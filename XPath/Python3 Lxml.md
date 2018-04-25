# Python3 Lxml

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
