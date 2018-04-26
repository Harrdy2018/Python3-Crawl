# W3school XPath实例用法

# 例子如下
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!--  Copyright w3school.com.cn -->
<!-- W3School.com.cn bookstore example -->
<bookstore>
<book category="children">
<title lang="en">Harry Potter</title>
<author>J K. Rowling</author>
<year>2005</year>
<price>29.99</price>
</book>
<book category="cooking">
<title lang="en">Everyday Italian</title>
<author>Giada De Laurentiis</author>
<year>2005</year>
<price>30.00</price>
</book>
<book category="web" cover="paperback">
<title lang="en">Learning XML</title>
<author>Erik T. Ray</author>
<year>2003</year>
<price>39.95</price>
</book>
<book category="web">
<title lang="en">XQuery Kick Start</title>
<author>James McGovern</author>
<author>Per Bothner</author>
<author>Kurt Cagle</author>
<author>James Linn</author>
<author>Vaidyanathan Nagarajan</author>
<year>2003</year>
<price>49.99</price>
</book>
</bookstore>
```
***[网址链接](http://www.w3school.com.cn/example/xmle/books.xml)*** <http://www.w3school.com.cn/example/xmle/books.xml>

***
# 第一步 运用爬虫知识获取网页信息
```python
import urllib.request
url='http://www.w3school.com.cn/example/xmle/books.xml'
req=urllib.request.Request(url)
response=urllib.request.urlopen(req)
```
```python
print(response.getcode())
print(response.geturl())
>>>
200
http://www.w3school.com.cn/example/xmle/books.xml
```
```python
print(response.info())
>>>
Content-Type: text/xml
Last-Modified: Mon, 29 Jul 2013 17:25:37 GMT
Accept-Ranges: bytes
ETag: "9449cba3808cce1:0"
Server: Microsoft-IIS/10.0
X-Powered-By: ASP.NET
Date: Thu, 26 Apr 2018 01:47:22 GMT
Connection: close
Content-Length: 896
```

***
* XPath路径选择以下面为基础
```python
print(response.read().decode('utf-8'))
>>>
<?xml version="1.0" encoding="ISO-8859-1"?>
<!--  Copyright w3school.com.cn -->
<!-- W3School.com.cn bookstore example -->
<bookstore>
<book category="children">
<title lang="en">Harry Potter</title>
<author>J K. Rowling</author>
<year>2005</year>
<price>29.99</price>
</book>
<book category="cooking">
<title lang="en">Everyday Italian</title>
<author>Giada De Laurentiis</author>
<year>2005</year>
<price>30.00</price>
</book>
<book category="web" cover="paperback">
<title lang="en">Learning XML</title>
<author>Erik T. Ray</author>
<year>2003</year>
<price>39.95</price>
</book>
<book category="web">
<title lang="en">XQuery Kick Start</title>
<author>James McGovern</author>
<author>Per Bothner</author>
<author>Kurt Cagle</author>
<author>James Linn</author>
<author>Vaidyanathan Nagarajan</author>
<year>2003</year>
<price>49.99</price>
</book>
</bookstore>
```

***
# 第二步  过一遍etree.tostring()序列化知识
```python
from lxml import etree
import urllib.request
url='http://www.w3school.com.cn/example/xmle/books.xml'
req=urllib.request.Request(url)
response=urllib.request.urlopen(req)
page=response.read()

root=etree.XML(text=page)#参数为二进制
print(etree.tostring(root,pretty_print=True).decode('utf-8'))
>>>
<bookstore>
<book category="children">
<title lang="en">Harry Potter</title>
<author>J K. Rowling</author>
<year>2005</year>
<price>29.99</price>
</book>
<book category="cooking">
<title lang="en">Everyday Italian</title>
<author>Giada De Laurentiis</author>
<year>2005</year>
<price>30.00</price>
</book>
<book category="web" cover="paperback">
<title lang="en">Learning XML</title>
<author>Erik T. Ray</author>
<year>2003</year>
<price>39.95</price>
</book>
<book category="web">
<title lang="en">XQuery Kick Start</title>
<author>James McGovern</author>
<author>Per Bothner</author>
<author>Kurt Cagle</author>
<author>James Linn</author>
<author>Vaidyanathan Nagarajan</author>
<year>2003</year>
<price>49.99</price>
</book>
</bookstore>
```

***
# 第三步  开始XPath
* lxml.etree.XML()返回一个容器，我们靠这个容器来XPath
```python
from lxml import etree
import urllib.request
url='http://www.w3school.com.cn/example/xmle/books.xml'
req=urllib.request.Request(url)
response=urllib.request.urlopen(req)
page=response.read()
root=etree.XML(text=page)#参数为二进制 
print(type(root))#<class 'lxml.etree._Element'>
```

***
* Ex.1 root.xpath('string()')
```python
#print(root.tag)#bookstore
print(root.xpath('string()'))
>>>


Harry Potter
J K. Rowling
2005
29.99


Everyday Italian
Giada De Laurentiis
2005
30.00


Learning XML
Erik T. Ray
2003
39.95


XQuery Kick Start
James McGovern
Per Bothner
Kurt Cagle
James Linn
Vaidyanathan Nagarajan
2003
49.99



```

***
* Ex.2 root.xpath('//text()')
```python
print(root.xpath('//text()'))
>>>
['\n', '\n', 'Harry Potter', '\n', 'J K. Rowling', '\n', '2005', '\n', '29.99', '\n', '\n', '\n', 'Everyday Italian', '\n', 'Giada De Laurentiis', '\n', '2005', '\n', '30.00', '\n', '\n', '\n', 'Learning XML', '\n', 'Erik T. Ray', '\n', '2003', '\n', '39.95', '\n', '\n', '\n', 'XQuery Kick Start', '\n', 'James McGovern', '\n', 'Per Bothner', '\n', 'Kurt Cagle', '\n', 'James Linn', '\n', 'Vaidyanathan Nagarajan', '\n', '2003', '\n', '49.99', '\n', '\n']
```

***
* Ex.3
```python
r1=root.xpath('bookstore')
print(r1)
>>>[]


r2=root.xpath('/bookstore')
print(r2)
print(r2[0].tag)
>>>
[<Element bookstore at 0x16eea529e88>]
bookstore


r3=root.xpath('bookstore/book')
print(r3)
>>>[]


r4=root.xpath('//book')
print(r4)
>>>
[<Element book at 0x1c5c7b6ae48>, <Element book at 0x1c5c7b6aec8>, <Element book at 0x1c5c7b6af08>, <Element book at 0x1c5c6b0cfc8>]


r5=root.xpath('bookstore//book')
print(r5)
>>>[]


r6=root.xpath('//@lang')
print(r6)
>>>['en', 'en', 'en', 'en']
```

***
* Ex.4 在容器里面进行XPath，如果路径以标签结束，那么返回一个列表，这个列表里面装了每个标签的Element
```python
r=root.xpath('/bookstore/book/title')
print(r)
print(type(r))
>>
[<Element title at 0x21bbf3a8ec8>, <Element title at 0x21bbf3a8e88>, <Element title at 0x21bbf3a8fc8>, <Element title at 0x21bbe32cfc8>]
<class 'list'>

for element in r:
    #print(element.tag)#title
    print(etree.tostring(element))
    print(element.text)
>>>
b'<title lang="en">Harry Potter</title>\n'
Harry Potter
b'<title lang="en">Everyday Italian</title>\n'
Everyday Italian
b'<title lang="en">Learning XML</title>\n'
Learning XML
b'<title lang="en">XQuery Kick Start</title>\n'
XQuery Kick Start
```
