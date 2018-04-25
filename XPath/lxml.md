# lxml

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
root_tag_name=etree.Element('root')
#XML元素的标签名可以通过tag property来访问
#print(root_tag_name.tag)#root
#Elements以XML tree structure进行组织。
#要创建child elements并将它们添加到parent element,可以使用append()方法
root_tag_name.append( etree.Element("child1") )
#为了看到真正的XML，你可以序列化(serialise)你创建的树
XML_binary=etree.tostring(root_tag_name, pretty_print=True)
print(XML_binary.decode('utf-8'))
>>>
<root>
  <child1/>
</root>
```

***
`SubElement factory能够使上面程序简化，它和Element factory有相同的参数，但是额外要求the parent作为第一个参数`
* Ex.2 改写Ex.1
```python
```
