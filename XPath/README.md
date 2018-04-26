# XPath
* [XML](#XML)
* 什么是 XML?
* 什么是 XPath?
* XPath 路径表达式
* [实战](#实战)

***
# XML
* XML 被设计用来传输和存储数据。
* HTML 被设计用来显示数据。

***
# 什么是 XML?
* XML 指可扩展标记语言（EXtensible Markup Language）
* XML 是一种标记语言，很类似 HTML
* XML 的设计宗旨是传输数据，而非显示数据
* XML 标签没有被预定义。您需要自行定义标签。
* XML 被设计为具有自我描述性。
* XML 是 W3C 的推荐标准

***
# 什么是 XPath?
* XPath 是一门在 XML 文档中查找信息的语言。XPath 用于在 XML 文档中通过元素和属性进行导航。
* XPath 使用路径表达式在 XML 文档中进行导航
* XPath 包含一个标准函数库
* XPath 是 XSLT 中的主要元素
* XPath 是一个 W3C 标准

***
# XPath 路径表达式
**XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。**





***
# 实战一
* 利用lxml.etree.parse()解析文件
* 新建hello.html
```html
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
```
***
```python
from lxml import etree
page=etree.parse('hello.html')
print(type(page))#<class 'lxml.etree._ElementTree'>
print(etree.tostring(page,pretty_print=True,method='html').decode())
>>>
<class 'lxml.etree._ElementTree'>
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
```

***
* Ex.1
```python
from lxml import etree
text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
#把字符串解析成HTML的样子
html=etree.HTML(text)
#print(type(html))#<class 'lxml.etree._Element'>
result=etree.tostring(html,pretty_print=True)
print(result.decode('utf-8'))
>>>
<html>
  <body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
</body>
</html>
>>>
>>>
>>>
#获取所有的 <li> 标签
r1=html.xpath('//li')
print(r1)
print(type(r1))
print(type(r1[0]))
print(r1[0].tag)
>>>
[<Element li at 0x26cf17d9a88>, <Element li at 0x26cf17d9a08>, <Element li at 0x26cf17d9b48>, <Element li at 0x26cf17d9b88>, <Element li at 0x26cf17d9bc8>]
<class 'list'>
<class 'lxml.etree._Element'>
li
>>>
>>>
>>>
#获取 <li> 标签的所有 class
r2=html.xpath('//li/@class')
print(r2)
>>>
['item-0', 'item-1', 'item-inactive', 'item-1', 'item-0']
>>>
>>>
>>>
#获取 <li> 标签下 href 为 link1.html 的 <a> 标签
r3 = html.xpath('//li/a[@href="link1.html"]')
print(r3)
>>>
[<Element a at 0x2c201de9a08>]
>>>
>>>
>>>
#获取 <li> 标签下的所有 <span> 标签
#因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
r4=html.xpath('//li//span')
print(r4)
print(r4[0].text)
>>>
[<Element span at 0x1b694119ac8>]
third item
>>>
>>>
>>>
#获取 <li> 标签下的所有 class，不包括 <li>
r5 = html.xpath('//li/a//@class')
print(r5)
>>>
['bold']
>>>
>>>
>>>
#获取最后一个 <li> 的 <a> 的 href
r6=html.xpath('/html/body/div/ul/li[last()]/a/@href')
print(r6)
>>>
['link5.html']
>>>
>>>
>>>
r66=html.xpath('//li[last()]/a/@href')
print(r66)
>>>
['link5.html']
>>>
>>>
>>>
#获取倒数第二个元素的内容
r7= html.xpath('//li[last()-1]/a')
print(r7[0].text)
>>>
fourth item
>>>
>>>
>>>
#获取 class 为 bold 的标签名
r8= html.xpath('//*[@class="bold"]')
print(r8[0].tag)
>>>
span
```

***
# 实战二
***使用lxml.etree.HTML()解析字符串***
```python
from lxml import etree
html="""
<!DOCTYPE html>
<html>
<head lang="en">
<title>测试</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body><div id="content">
<ul id="ul">
    <li>NO.1</li>
    <li>NO.2</li>
    <li>NO.3</li>
</ul>
<ul id="ul2">
    <li>one</li>
    <li>two</li>
</ul>
</div>
<div id="url">
    <a href="http:www.58.com" title="58">58</a>
    <a href="http:www.csdn.net" title="CSDN">CSDN</a>
</div></body></html>
"""

#返回的是容易对象，在我写的这些东西里面，我通常把返回的容器对象叫做root，下面是另外一种称呼，叫做选择器，似乎更加贴切
selector=etree.HTML(html)

#这里使用id属性来定位哪个div和ul被匹配 使用text()获取文本内容
r1=selector.xpath('//div[@id="content"]/ul[@id="ul"]/li/text()')
print(r1)
>>>['NO.1', 'NO.2', 'NO.3']

#这里使用//从全文中定位符合条件的a标签，使用“@标签属性”获取a便签的href属性值
r2=selector.xpath('//a/@href')
print(r2)
>>>['http:www.58.com', 'http:www.csdn.net']

#使用绝对路径定位a标签的title
r3=selector.xpath('/html/body/div/a/@title')
print(r3)
>>>['58', 'CSDN']

#使用相对路径定位 两者效果是一样的
r4=selector.xpath('//a/@title')
print(r4)
>>>['58', 'CSDN']
```

***
* 先对字符串做一个选择器
```python
from lxml import etree
html='''
<body>
    <div id="aa">aa</div>
    <div id="ab">ab</div>
    <div id="ac">ac</div>
</body>
'''
selector=etree.HTML(html)


#我们尝试使用序列化，看看效果
print(etree.tostring(selector,pretty_print=True).decode('utf-8'))
>>>
<html><body>
    <div id="aa">aa</div>
    <div id="ab">ab</div>
    <div id="ac">ac</div>
</body>
</html>
#我们可以发现如果是一个不完整的网页字符串对象，那么这个函数会帮我们补全
#尝试加method方法
print(etree.tostring(selector,pretty_print=True,method='html').decode('utf-8'))
>>>
<html>
<body>
    <div id="aa">aa</div>
    <div id="ab">ab</div>
    <div id="ac">ac</div>
</body>
</html>
#我们又发现了不一样，method方法帮助我们格式化之后变成了最标准的网页


#开始XPath
#starts-with 解决标签属性值以相同字符串开头的情况
#这里使用starts-with方法提取div的id标签属性值开头为a的div标签
r1=selector.xpath('//div[starts-with(@id,"a")]/text()')
print(r1)
>>>['aa', 'ab', 'ac']
```

***
# 实战三
***string(.) 标签套标签***
```python
from lxml import etree
html='''<div id="a">left<span id="b">right<ul>up<li>down</li></ul>east</span>west</div>'''
selector=etree.HTML(html)
r=selector.xpath('//div[@id="a"]/text()')
print(r)
>>>['left', 'west']


r2=selector.xpath('//div[@id="a"]')[0].xpath('string(.)')
print(r2)
>>>leftrightupdowneastwest
```
