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
|:-----|:-----|
|selector.xpath('/bookstore')|绝对路径选取根元素bookstore|
|selector.xpath('/bookstore/book')|bookstore的子元素的所有book元素|
|selector.xpath('//book')|相对路径选取所有book子元素，而不管它们在文档中的位置|
|selector.xpath('/bookstore//book')|bookstore元素的后代的所有book元素，而不管它们位于bookstore之下的什么位置|
|selector.xpath('//@lang')|lang的所有属性|

***
**总结：只有Element对象才能作为选择器（目前只接触到这个）；选择器经过路径选择后，永远返回一个列表；如果路径选择以选择标签节点为目的，则返回Element对象的列表；如果以属性键结束，则返回属性值的列表**

***
## 谓语
***Predicates，谓语用来查找某个特定的节点或者包含某个指定的值的节点。谓语被嵌在方括号中***
***
|path|功能|
|:-----|:-----|
|selector.xpath('/bookstore/book[1]')|bookstore子元素的第一个book元素|
|selector.xpath('/bookstore/book[last()]')|bookstore子元素的最后一个book元素|
|selector.xpath('/bookstore/book[last()-1]')|bookstore子元素的倒数第二个book元素|
|selector.xpath('/bookstore/book[position()<3]')|最前面的两个属于bookstore元素的子元素的book元素|
|selector.xpath('//title[@lang]')|所有拥有名为lang的属性的title元素|
|selector.xpath('//title[@lang='eng']')|所有title元素，且这些元素拥有值为eng的lang属性|
|selector.xpath('/bookstore/book[price>35.00]')|bookstore元素的所有book元素，且其中的price元素的值须大于35.00|
|selector.xpath('/bookstore/book[price>35.00]/title')|bookstore元素中的book元素的所有title元素，且其中的price元素的值须大于35.00|

***
## 通配符选取未知节点
|path|功能|
|:-----|:-----|
|`selector.xpath('/bookstore/*')`|选取bookstore元素的所有子元素|
|`selector.xpath('//*')`|选取文档中的所有元素|
|`selector.xpath('//title[@*]')`|选取所有带有属性的title元素|
