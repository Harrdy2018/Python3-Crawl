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
* 文档节点<bookstore>
* 元素节点<author>J K. Rowling</author>
* 属性节点lang="en"
* parent book元素是title、author、year以及price元素的父
* children title、author、year以及price元素都是book元素的子
* sibling  title、author、year以及price元素都是同胞
* ancestor 某节点的父、父的父，等等。title元素的先辈是book元素和bookstore元素
* descendant 某个节点的子，子的子，等等。bookstore的后代是book、title、author、year 以及 price 元素
