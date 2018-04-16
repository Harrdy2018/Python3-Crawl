#由于在表单的提交过程中，表单中的salt和sign两个值随着时间戳在变化，需要花点时间读懂有道翻译源码中的JS代码，弄清楚有道翻译的加密机制，才能写出正确代码
#下面代码只是一种思维方式，程序本身运行有错误，等时间充足过来修正！！
import urllib.request
import urllib.parse
def main():
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data={}
    data['i']="I love you!"
    data['from']="en"
    data['to']='zh - CHS'
    data['smartresult']='dict'
    data["client"]='fanyideskweb'
    data['salt']='1523757893496'
    data['sign']='981abe78463f8253a31e5676a3a5b31a'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLICKBUTTION'
    data['typoResult']='false'
    data=urllib.parse.urlencode(data)
    data=data.encode('utf-8')
    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')
if __name__=="__main__":
    main()
