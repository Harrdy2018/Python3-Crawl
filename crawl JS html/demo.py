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
url='http://pycoders.com/archive/'
r=Render(url)

result=r.frame.toHtml()
formatted_result=str(ascii(result))
tree = html.fromstring(formatted_result)
archive_links = tree.xpath('//div[@class="campaign"]/a/@href')
for item in archive_links:
    print(item)
