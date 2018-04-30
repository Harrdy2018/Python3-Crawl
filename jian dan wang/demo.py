import urllib.request
from multiprocessing.pool import Pool
from lxml import html
import sys,os,time
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

def initialize():
    #初始化文件夹
    if os.path.exists(path='ooxx'):
        pass
    else:
        os.mkdir(path='ooxx', mode=0o777)
    # print(os.getcwd())
    os.chdir('ooxx')
    #print(os.getcwd())

def get_sign(url):
    #得到当前页面的标记
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    req=urllib.request.Request(url=url,headers=header)
    response=urllib.request.urlopen(req)
    page=response.read().decode('utf-8')

    tree=html.fromstring(html=page)
    r=tree.xpath('//div[@class="cp-pagenavi"]/span[@class="current-comment-page"]/text()')
    return r[0].split('[')[1].split(']')[0]

def page_url(ur1,num,sign):
    #根据您输入的页面数字，把没一张页面的url存入列表中
    urls=[]
    for i in range(num):
        urls.append('{0}/page-{1}#comments'.format(url,sign-i))
    return urls

def save_mm(url):
    response = urllib.request.urlopen(url)
    mm_img = response.read()
    with open(str(time.time())+url[-4:], 'wb') as f:
        f.write(mm_img)

def parse_OnePage(url):
    print("child process %s run..." % os.getpid())
    class Render(QWebPage):
        def __init__(self, url):
            self.app = QApplication(sys.argv)
            QWebPage.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.mainFrame().load(QUrl(url))
            self.app.exec_()

        def _loadFinished(self, result):
            self.frame = self.mainFrame()
            self.app.quit()

    # This does the magic.Loads everything.
    r = Render(url)
    result = r.frame.toHtml()
    # Result is a QString.

    # QString should be converted to string before processed by lxml
    formatted_result = str(ascii(result))

    # Next build lxml tree from formatted_result
    tree = html.fromstring(formatted_result)

    # Now using correct Xpath we are fetching URL of archives
    mm_links = tree.xpath('//li//p/img/@src')
    for mm in mm_links:
        save_mm(mm)
    print("child process %s end..." % os.getpid())


if __name__=="__main__":
    print("parent process %s run..."% os.getpid())
    initialize()
    url='http://jandan.net/ooxx'
    sign=get_sign(url)

    num=int(input("您需要下载多少页>>>"))
    mm_url=page_url(url,num,int(sign))

    p=Pool(processes=2)
    for i in range(len(mm_url)):
        p.apply_async(func=parse_OnePage,args=(mm_url[i],))
    p.close()
    p.join()
    print("parent process %s end..." % os.getpid())
