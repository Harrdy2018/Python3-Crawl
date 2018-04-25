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
# 实战
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
* 
