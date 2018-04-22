# 代理
***代理（proxy）***
 
 
 
## 为什么要使用代理
```上一次我们理解了爬虫隐藏客户端请求头的策略，但是服务器也会作相应的反爬虫策略，比如计算提交的频率，如果频率超过，就不让你提交了，
怎么样改进方法呢，延迟提交就出现了
import time
time.sleep(5)//让程序每运行一次先睡5秒
但是这样改进之后，和浏览器访问没什么两样，所以我们需要多个小伙伴来协助我，然后小伙伴把爬到的信息全部发给我，这就是代理
```

***
## 怎么样获取代理IP和查询IP
* [查询IP地址](http://ip.chinaz.com/getip.aspx):`http://ip.chinaz.com/getip.aspx`
* [国内代理网址](http://www.xicidaili.com/nn/):`http://www.xicidaili.com/nn/`
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
`urllib.request.install_opener(opener)`<br>
* 调用opener
opener.open(url)

###example
在网上查代理IP地址http://www.xicidaili.com/   https://www.kuaidaili.com/free/

import urllib.request
url="http://www.whatismyip.com.tw"
proxy_support=urllib.request.ProxyHandler({'http':'14.221.165.121:9797'})
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0')]
urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
