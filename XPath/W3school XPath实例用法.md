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
