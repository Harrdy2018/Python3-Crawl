#谷歌翻译 英语转汉语
import requests
import execjs #必须要先用pip 安装，用来执行js脚本
class Py4Js():
  def __init__(self):
    self.ctx = execjs.compile(""" 
    function TL(a) { 
    var k = ""; 
    var b = 406644; 
    var b1 = 3293161072;       
    var jd = "."; 
    var $b = "+-a^+6"; 
    var Zb = "+-3^+b+-f";    
    for (var e = [], f = 0, g = 0; g < a.length; g++) { 
        var m = a.charCodeAt(g); 
        128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
        e[f++] = m >> 18 | 240, 
        e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
        e[f++] = m >> 6 & 63 | 128), 
        e[f++] = m & 63 | 128) 
    } 
    a = b; 
    for (f = 0; f < e.length; f++) a += e[f], 
    a = RL(a, $b); 
    a = RL(a, Zb); 
    a ^= b1 || 0; 
    0 > a && (a = (a & 2147483647) + 2147483648); 
    a %= 1E6; 
    return a.toString() + jd + (a ^ b) 
  };      
  function RL(a, b) { 
    var t = "a"; 
    var Yb = "+"; 
    for (var c = 0; c < b.length - 2; c += 3) { 
        var d = b.charAt(c + 2), 
        d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
        d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
        a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
    } 
    return a 
  } 
 """)
  def getTk(self,text):
      return self.ctx.call("TL",text)

def translate(text):
    url='https://translate.google.cn/translate_a/single'
    headers = {
        'user-agent': 'Mozilla/5.0'
    }
    tk_value=js.getTk(text)
    data={
        'client':'t',
        'sl':'en',
        'tl':'zh-CN',
        'hl':'zh-CN',
        'dt':['at','bd','ex','ld','md','qca','rw','rm','ss','t'],
        'ie':'UTF-8',
        'oe':'UTF-8',
        'source':'btn',
        'ssel':'3',
        'tsel':'6',
        'kc':'14',
        'tk':str(tk_value),
        'q':text
    }
    get_url=(url+"?client={0}&sl={1}&tl={2}&hl={3}&dt={4}&dt={5}&dt={6}&dt={7}&dt={8}&dt={9}&dt={10}&dt={11}&dt={12}&dt={13}&ie={14}&oe={15}&source={16}&ssel={17}&tsel={18}&kc={19}&tk={20}&q={21}").format(data['client'],data['sl'],data['tl'],data['hl'],data['dt'][0],data['dt'][1],data['dt'][2],data['dt'][3],data['dt'][4],data['dt'][5],data['dt'][6],data['dt'][7],data['dt'][8],data['dt'][9],data['ie'],data['oe'],data['source'],data['ssel'],data['tsel'],data['kc'],data['tk'],data['q'])
    response=requests.get(get_url,headers)
    return response
if __name__ == '__main__':
  js=Py4Js()
  print("\t\t\t\t\tGoogle Translating Machine Made By Kang Lu")
  s=input("英译汉，请输入要翻译的英语语句>>>")
  response=translate(s)
  print('正在翻译>>>{0}'.format(response.json()[0][0][1]))
  print(response.json()[0][0][0])
