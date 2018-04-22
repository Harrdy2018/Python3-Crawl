#服务器也会作相应的反爬虫策略，比如计算提交的频率，如果频率超过，就不让你提交了，改进方法，延迟提交
import time
time.sleep(5)//让程序每运行一次先睡5秒
#代理
#步骤:
一，参数是一个字典{‘类型’：‘代理IP：端口号’}
class urllib.request.ProxyHandler(proxies=None)
proxy_support=urllib.request.ProxyHandler({})
二，定制、创建一个opener
#私人定制
opener=urllib.request.build_opener(proxy_support)
三，安装opener
urllib.request.install_opener(opener)
调用opener
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
