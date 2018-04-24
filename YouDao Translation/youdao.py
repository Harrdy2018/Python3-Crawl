import urllib.request
import urllib.parse
import time
import random
import hashlib
import json
def translate(word,url,salt,sign):
    #向服务器提交的表单数据，以post方式提交
    form_data={
        'i': word,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION',
        'typoResult':'false'
    }
    #处理表单数据
    form_data = urllib.parse.urlencode(form_data).encode('utf-8')
    #隐藏
    head = {}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    #构建Request对象
    req = urllib.request.Request(url,data=form_data,headers=head)
    #服务器返回
    response = urllib.request.urlopen(req)
    #打印一些服务器返回的信息
    #print(response.getcode())
    #print(response.info())
    #print(response.geturl())
    transresult = response.read().decode('utf-8')
    #print(transresult)
    #将json数据转化为dict类型
    result_dict=json.loads(transresult)
    return result_dict['translateResult'][0][0]['tgt']
def decipher(word):
    # js代码加密salt   r = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
    # js代码加密sign i = n.md5("fanyideskweb" + t + r + "ebSeFb%=XZ%T[KZ)c(sy!");
    salt_value=str(int(time.time() * 1000) + random.randint(0, 10))
    u = "fanyideskweb"
    t = word
    r = salt_value
    s = "ebSeFb%=XZ%T[KZ)c(sy!"
    #加密三部曲
    md=hashlib.md5()
    md.update((u + t + r + s).encode('utf-8'))
    sign_value=md.hexdigest()
    return salt_value,sign_value
def main():
    print("本程序实现中英互翻译！！！")
    word = input("请输入您要翻译的句子>>>")
    salt,sign=decipher(word)
    print("发送给服务器的salt字符串：",salt)
    print("发送给服务器的sign字符串",sign)
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    result=translate(word,url,salt,sign)
    print(result)
if __name__=="__main__":
    main()
