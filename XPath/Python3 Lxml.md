# Python3 Lxml
* lxml
* The Element class
* Elements are lists
* Elements carry attributes as a dict
* Elements contain text
* Using XPath to find text

***[lxml - XML and HTML with Python](http://lxml.de/)***

***
# lxml
```
lxml是用于在Python语言中处理XML和HTML的功能最丰富且易于使用的库。
feature-rich功能丰富的
easy-to-use易于使用的
```

# The Element class
```
Element是ElementTree API的主要容器对象(container object)。 大多数XML树功能都是通过这个类来访问的。
Elements可以通过元素工厂(the Element factory)轻松创建
```

***
* Ex.1
```python
from lxml import etree
#创建根元素，标签名为body
root=etree.Element('body')
#XML元素的标签名可以通过tag property来访问
print(root.tag)#body
#Elements以XML tree structure进行组织。
#要创建child elements并将它们添加到parent element,可以使用append()方法
root.append(etree.Element("div1"))
#为了看到真正的XML，你可以序列化(serialise)你创建的树
XML_binary=etree.tostring(root, pretty_print=True)
print(XML_binary.decode('utf-8'))
>>>
body
<body>
  <div1/>
</body>
```

***
`SubElement factory能够使上面程序简化，它和Element factory有相同的参数，但是额外要求the parent作为第一个参数`
* Ex.2 改写Ex.1
```python
from lxml import etree
root=etree.Element('body')
child1=etree.SubElement(root,'div1')
child2=etree.SubElement(root,'div2')
child3=etree.SubElement(root,'div3')
XML_binary=etree.tostring(root, pretty_print=True)
print(XML_binary.decode('utf-8'))
>>>
<body>
  <div1/>
  <div2/>
  <div3/>
</body>
```

***
# Elements are lists
```
为了简单直接地访问subelements，元素尽可能地模仿正常Python列表的行为
```
* Ex.1
```python
from lxml import etree
root=etree.Element('body')
child1=etree.SubElement(root,'div1')
child2=etree.SubElement(root,'div2')
child3=etree.SubElement(root,'div3')
print(root[0].tag)#div1
print(len(root))#3
print(root.index(root[1]))#1

children=list(root)
for child in children:
    print(child.tag)
#div1
#div2
#div3

root.insert(0, etree.Element("div0"))
start=root[:1]
end= root[-1:]
print(start[0].tag)#div0
print(end[0].tag)#div3
```

***
* Ex.2 判断元素是否有子元素
```python
from lxml import etree
root=etree.Element('body')
child1=etree.SubElement(root,'div1')
child2=etree.SubElement(root,'div2')
child3=etree.SubElement(root,'div3')
# test if it's some kind of Element
print(etree.iselement(root))
# test if it has children
if len(root):
   print("The root element has children")
>>>
True
The root element has children
```

***
* Ex.3.1 元素列表里的赋值，即删除
```python
from lxml import etree
root=etree.Element('body')
child1=etree.SubElement(root,'div1')
child2=etree.SubElement(root,'div2')
child3=etree.SubElement(root,'div3')

for child in root:
    print(child.tag)
root[0]=root[-1]
print('***************')
for child in root:
    print(child.tag)
>>>
div1
div2
div3
***************
div3
div2
```

* Ex.3.2 python列表赋值
```python
data=[1,2,3,4]
data[0]=data[-1]
print(data)
>>>
[4, 2, 3, 4]
```

***
* Ex.4
```python
from lxml import etree
root=etree.Element('body')
child1=etree.SubElement(root,'div1')
child2=etree.SubElement(root,'div2')
child3=etree.SubElement(root,'div3')
print(root is root[0].getparent())# lxml.etree only!
print(root[0] is root[1].getprevious())# lxml.etree only!
print(root[1] is root[0].getnext())# lxml.etree only!
>>>
True
True
True
```

***
# Elements carry attributes as a dict
```
XML elements支持attributes.你能在the Element factory直接创建他们
```
* Ex.1
```python
from lxml import etree
root = etree.Element("body", interesting="totally")
XML_binary=etree.tostring(root)
print(XML_binary)
>>>
b'<body interesting="totally"/>'
```

***
* Ex.2 Attributes只是无序的name-value pairs，因此处理它们的一种非常方便的方式就是通过像字典一样的元素接口
```python
from lxml import etree
root = etree.Element("body", interesting="totally")
etree.tostring(root)
print(root.get('interesting'))
>>>totally
print(root.get("hello"))
>>>None
root.set("hello", "Huhu")
print(root.get("hello"))
>>>Huhu
print(etree.tostring(root))
>>>b'<body interesting="totally" hello="Huhu"/>'
print(sorted(root.keys()))
>>>['hello', 'interesting']
for name, value in sorted(root.items()):
    print('%s = %r' % (name, value))
>>>hello = 'Huhu'
interesting = 'totally'
```

***
* Ex.3 对于想要进行项查找或有其他原因需要获得“真正”类似字典的对象的情况，你可以使用attrib property
```python
from lxml import etree
root = etree.Element("body", interesting="totally")
attributes = root.attrib
print(attributes["interesting"])
print(attributes.get("no-such-attribute"))
attributes["hello"] = "Guten Tag"
print(attributes["hello"])
print(root.get("hello"))
>>>
totally
None
Guten Tag
Guten Tag
```

***
* Ex.4 要获取不依赖于XML树的属性的独立快照，请将其复制到字典中
```python
from lxml import etree
root = etree.Element("body", interesting="totally")
attributes = root.attrib
attributes["hello"] = "Guten Tag"
d = dict(attributes)
print(sorted(d.items()))
>>>
[('hello', 'Guten Tag'), ('interesting', 'totally')]
```

***
# Elements contain text
* Ex.1 元素能包含文本
```python
from lxml import etree
root = etree.Element("body")
root.text = "TEXT"
print(root.text)
print(etree.tostring(root))
>>>
TEXT
b'<body>TEXT</body>'
```
```
在许多XML文档（以数据为中心的文档）中，这是唯一可以找到文本的地方。 它由叶子标签封装在树层次结构的最底部。
但是，如果将XML用于标记的文本文档（如HTML），则文本也可以出现在不同元素之间，即在树的中间
<html><body>Hello<br/>World</body></html>
这里，<br/>标签被文字包围。 这通常被称为文档样式或混合内容XML。 
元素通过它们的尾部属性支持它。 它包含直接跟随元素的文本，直到XML树中的下一个元素：
```
```python
from lxml import etree
root=etree.Element('html')
child1=etree.SubElement(root,'body')
child1.text='TEXT'
child2=etree.SubElement(child1,'br')
child2.tail='TALL'
print(etree.tostring(root))

print(etree.tostring(child2))
print(etree.tostring(child2, with_tail=False))

#如果你仅仅需要文本，而不需要任何中间标签
print(etree.tostring(root, method="text"))
>>>
b'<html><body>TEXT<br/>TALL</body></html>'
b'<br/>TALL'
b'<br/>'
b'TEXTTALL'
```

***
# Using XPath to find text
**提取树的文本内容的另一种方法是XPath，它还允许您将单独的文本块提取到列表中：**
```python
from lxml import etree
root=etree.Element('html')
child1=etree.SubElement(root,'body')
child1.text='TEXT'
child2=etree.SubElement(child1,'br')
child2.tail='TALL'
print(etree.tostring(root))

print(root.xpath("string()"))
print(root.xpath("//text()"))
>>>
b'<html><body>TEXT<br/>TALL</body></html>'
TEXTTALL
['TEXT', 'TALL']
```

**如果你想更频繁地使用它，你可以把它包装在一个函数中**
```python
from lxml import etree
root=etree.Element('html')
child1=etree.SubElement(root,'body')
child1.text='TEXT'
child2=etree.SubElement(child1,'br')
child2.tail='TALL'
print(etree.tostring(root))

build_text_list = etree.XPath("//text()")
print(build_text_list(root))
>>>
b'<html><body>TEXT<br/>TALL</body></html>'
['TEXT', 'TALL']
```

**请注意，XPath返回的字符串结果是一个知道其起源的特殊“智能”对象。你可以通过它的getparent()方法来问它来自哪里，就像你使用Elements一样**
```python
from lxml import etree
root=etree.Element('html')
child1=etree.SubElement(root,'body')
child1.text='TEXT'
child2=etree.SubElement(child1,'br')
child2.tail='TALL'
print(etree.tostring(root))

build_text_list = etree.XPath("//text()")
texts = build_text_list(root)
print(texts[0])
parent = texts[0].getparent()
print(parent.tag)
print(texts[1])
print(texts[1].getparent().tag)

#find out if it's normal text content or tail text
print(texts[0].is_text)
print(texts[1].is_text)
print(texts[1].is_tail)

#虽然这适用于text()函数的结果
#但lxml不会告诉您由XPath函数string()或concat()构造的字符串值的来源
stringify = etree.XPath("string()")
print(stringify(root))
print(stringify(root).getparent())
>>>
b'<html><body>TEXT<br/>TALL</body></html>'
TEXT
body
TALL
br
True
False
True
TEXTTALL
None
```
