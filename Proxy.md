# 代理
***代理（proxy）***
* [为什么要使用代理](#为什么要使用代理)
* [怎么样获取代理IP和查询IP](#怎么样获取代理IP和查询IP)
* [创建代理步骤](#创建代理步骤)
* [使用代理例子](#使用代理例子)
* [总结](#使用代理例子)
 
***
## 为什么要使用代理
```上一次我们理解了爬虫隐藏客户端请求头的策略，但是服务器也会作相应的反爬虫策略，比如计算提交的频率，如果频率超过，就不让你提交了，
怎么样改进方法呢，延迟提交就出现了
import time
time.sleep(5)//让程序每运行一次先睡5秒
但是这样改进之后，和浏览器访问没什么两样，所以我们需要多个小伙伴来协助我，然后小伙伴把爬到的信息全部发给我，这就是代理
```

***
## 怎么样获取代理IP和查询IP
* [查询本地真实IP地址](http://ip.chinaz.com/getip.aspx):`http://ip.chinaz.com/getip.aspx`
* [返回当前IP地址](http://icanhazip.com):`http://icanhazip.com`
* [国内HTTP代理](http://www.xicidaili.com/wt/):`http://www.xicidaili.com/wt/`
* [测试IP国外代理](http://www.ip181.com):`http://www.ip181.com`

***
## 创建代理步骤
* 参数是一个字典{‘类型’：‘代理IP：端口号’}
```
class urllib.request.ProxyHandler(proxies=None)
proxy_support=urllib.request.ProxyHandler({})
```
* 定制、创建一个opener 私人定制
```
opener=urllib.request.build_opener(proxy_support)
```
* 安装opener
```
urllib.request.install_opener(opener)
```
* 调用opener
```
opener.open(url)
```

***
## 使用代理例子
* Ex.1 显示自己真正的IP地址
```python
import urllib.request
url="http://ip.chinaz.com/getip.aspx"
proxy={'http':'113.12.72.24:3128'}
proxy_support=urllib.request.ProxyHandler(proxy)
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
>>>{ip:'218.2.216.5',address:'江苏省南京市 南京邮电大学'}
```
```
爬取会经常被封ip。当自己的ip被网站封了之后，只能采取换代理ip的方式进行爬取，
所以，我建议，每次爬取的时候尽量用代理来爬，封了代理，还有代理，无穷无尽啊，可别拿代理去黑学校网站啊，扔上代理的实现程序
```
* Ex.2 显示代理IP地址
```python
import urllib.request
url="http://icanhazip.com"
proxy={'http':'113.12.72.24:3128'}
proxy_support=urllib.request.ProxyHandler(proxy)
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
>>>113.12.72.24
```
```
这里采用的测试网站是http://icanhazip.com， 它可以检测出你使用的ip是什么，正好来检验自己是否用代理ip成功
从结果中可以看出，检测出了代理ip，正是我自己加上的ip值，此乃最后一招，当自己ip被封后，采用代理ip进行访问。
要是一个代理ip挂了怎么办，那你可以做个ip池啊，就是把一堆代理ip放在一起，每次运行时从ip池挑一个代理ip当做访问ip就可以了！！！
```
* Ex.3 IP池
```python
import urllib.request
import random
url="http://icanhazip.com"
ip_list=['58.252.6.165:9000','113.12.72.24:3128']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(ip_list)})
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
```
* Ex.4 使用第三方库
```python
import requests
url='http://icanhazip.com'
proxy = {'http': '58.252.6.165:9000'}
head = {'User-Agent': 'Mozilla/5.0'}
r= requests.get(url, headers=head, proxies=proxy)
print(r.text)
>>>58.252.6.165
```
***这我就不知道了，明明使用了代理，为什么返回的还是我真正的IP地址，有待高手来帮我解决***

***
## 总结
**访问的IP查询网站用的是HTTP的协议，那么你的代理用的是也一定要是HTTP协议**<br>
**在使用第三方库设置代理时，用大写的`HTTP`会导致查到的一直是你的真实IP地址，用小写的`http`就会成功，我也不知道原因！！**
