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
* 安装PyQt4库 [Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)
