#伪装浏览器访问服务器
#解析URL请求的类
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None) 
#在正常用pyhthon3访问服务器
import urllib.request
def main():
    url='http://fanyi.youdao.com'
    req=urllib.request.Request(url)
    print(req.headers)
if __name__=="__main__":
    main()
>>>{}
#伪装浏览器访问服务器
import urllib.request
def main():
    url='http://fanyi.youdao.com'
    head={}
    head['User-Agent']='Mozilla/5.0'
    req=urllib.request.Request(url,headers=head)
    print(req.headers)
if __name__=="__main__":
    main()
>>>{'User-agent': 'Mozilla/5.0'}
#第二种方法改变请求头
import urllib.request
def main():
    url='http://fanyi.youdao.com'
    req=urllib.request.Request(url,headers={})
    req.add_header('User-Agent','Mozilla/5.0')
    print(req.headers)
if __name__=="__main__":
    main()
>>>{'User-agent': 'Mozilla/5.0'}

#总结---修改headers的方法
一，通过Request的headers参数修改
二，通过Request.add_header()方法修改
