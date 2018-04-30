# 爬JavaScript渲染过的网页

# 目标网站
[pycoder's weekly](http://pycoders.com/archive/)  `http://pycoders.com/archive/`
***
![](https://github.com/Harrdy2018/Python3-Crawl/blob/master/crawl%20JS%20html/pycoders.png)
***
**我们现在要爬取该网站下面的每周python事件的链接地址，下面用一般方法处理**
```python
from lxml import html
import urllib.request
req=urllib.request.Request(url)
response=urllib.request.urlopen(req)
text=response.read().decode('utf-8')
tree=html.fromstring(text)
print(tree)
>>><Element html at 0x2076e20fc28>

print(type(tree))
>>><class 'lxml.html.HtmlElement'>

r=tree.xpath('//div[@class="campaign"]/a/@href')
print(r)
>>>[]
```
**由于经过了js渲染，我们根本无法得到任何信息**

***
# 解决方案
```
Web kit 可以实现浏览器所能处理的任何事情。对于某些浏览器来说，Web kit就是其底层的网页渲染工具。
Web kit 是QT库的一部分，因此如果你已经安装QT和PyQT4库，那么你可以直接运行之。
```
* 安装PyQt4库 [Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
* 类Render可以用来渲染网页
```python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *

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
```
* 当我们新建一个Render类时，它可以将url中的所有信息加载下来并存到一个新的框架中
```python
url='http://pycoders.com/archive/'
# This does the magic.Loads everything.
r=Render(url)
result=r.frame.toHtml()
# Result is a QString.
```
* 利用以上的代码我们将 HTML 结果储存到变量result中，由于lxml无法直接处理该特殊的字符串数据，因此我们需要转换数据格式
```python
# QString should be converted to string before processed by lxml
formatted_result=str(ascii(result))

# Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

# Now using correct Xpath we are fetching URL of archives
archive_links = tree.xpath('//div[@class="campaign"]/a/@href')
for item in archive_links:
    print(item)
```
* 程序输出
```text
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=f203eb15cf
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=bb793fb200
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=99f7f43e06
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=7596c9d73a
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=85fc237433
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=4ad15dbd6a
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=62805321c8
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=e61e306040
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=90fd0654b1
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=f0ec67ef76
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=32fe872169
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=db760c54cb
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=07723115d0
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=ddee8d1479
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=3ca35b21b2
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=626db6c90c
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=83181648d6
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=4018ed7312
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=18f013f645
http://us4.campaign-archive.com/?u=9735795484d2e4c204da82a29&id=11db73cdfc
...
...
...
```
