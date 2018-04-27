# XPath教程

# XPath 术语
## 节点（Node）
```
在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。
XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。
```
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
<book>
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>
</bookstore>
```
***
* 文档节点 `<bookstore>`
* 元素节点 `<author>J K. Rowling</author>`
* 属性节点 `lang="en"`
* `parent` book元素是title、author、year以及price元素的父
* `children` title、author、year以及price元素都是book元素的子
* `sibling`  title、author、year以及price元素都是同胞
* `ancestor` 某节点的父、父的父，等等。title元素的先辈是book元素和bookstore元素
* `descendant` 某个节点的子，子的子，等等。bookstore的后代是book、title、author、year 以及 price 元素

# XPath语法
XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。
## 构造实例
```python
from lxml import etree
xml='''
<bookstore>
<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>
<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>
</bookstore>
'''
print(xml)
selector=etree.XML(xml)
print(type(selector))#<class 'lxml.etree._Element'>
print(etree.tostring(selector).decode('utf-8'))
```
**lxml.etree._Element才有资格作为选择器**<br>
**另外用HTML()解析字符串得到的效果是不一样的，它还按照html方式补全了标签的**<br>
**提供实例如下**
```string
<bookstore>
<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>
<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>
</bookstore>
```

***
## 选取节点
***
|path|功能|
|:-----:|:-----:|
|selector.xpath('/bookstore')|绝对路径选取根元素bookstore|
|selector.xpath('/bookstore/book')|bookstore的子元素的所有book元素|
|selector.xpath('//book')|相对路径选取所有book子元素，而不管它们在文档中的位置|
|selector.xpath('/bookstore//book')|bookstore元素的后代的所有book元素，而不管它们位于bookstore之下的什么位置|
