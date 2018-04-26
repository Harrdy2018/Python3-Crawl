from lxml import etree
import urllib.request
def get_html(url):
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    req=urllib.request.Request(url,headers=head)
    response=urllib.request.urlopen(req)
    #print(response.getcode())
    #print(response.geturl())
    return response.read()
def per_page_bank_info(url,bank_type,page_num):
    url=url+'?Province=&City=&Xian=&bankType={0}&cBankName=&cAddr=&search=true&page={1}'.format(bank_type,page_num)
    html=get_html(url).decode('utf-8')
    selector=etree.HTML(text=html)
    #第一步提取标题
    title=selector.xpath('//tr[@class="gary"]/td/text()')
    #print(title)#['序号', '行号', '网点名称', '电话', '地址']
    tr=selector.xpath('//form/table/tr[position()>5]')
    all_bank_info=[]
    for element in tr:
        td=element.xpath('child::td')
        row=[]
        for child in td:
            row.append(child.text)
        all_bank_info.append(row)
    return all_bank_info
def bank_name_type(html):
    selector=etree.HTML(text=html)
    #第一种方法提取信息
    bank_name=selector.xpath('//td/select[@id="bankType"]/option[position()>1]/text()')
    bank_type=selector.xpath('//td/select[@id="bankType"]/option[position()>1]/@value')
    #print(bank_name)
    #print(bank_type)
    '''
    #第二种方法提取
    r1=selector.xpath('//td/select[@id="bankType"]/option[position()>1]')
    #提取bank_name
    bank_name=[]
    for element in r1:
        #print(element.tag)#option 表示元素指向的是option标签
        bank_name.append(element.text)
        #bank_name.append(element.xpath('string()'))
    print(bank_name)
    '''
    return bank_name,bank_type
def main():
    url='http://furhr.com/'
    html=get_html(url).decode('utf-8')
    bank_name,bank_type=bank_name_type(html)

    bank_num=len(bank_name)
    for i in range(bank_num):
        print(bank_name[i])
    user_bank_name=input('请根据上述银行，正确输入您想要查找银行的全称>>>').strip()
    user_page_num=input('您需要多少页的信息量>>>').strip()
    user_bank_type=bank_type[bank_name.index(user_bank_name)]

    bank=[]
    for i in range(1,int(user_page_num)+1):
        per_record=per_page_bank_info(url,user_bank_type,i)
        #print(per_record)
        #判断列表为空，if(list),if(list==[]),if(len(list)==0)
        if(per_record):
            pass
        else:
            break
        bank.extend(per_page_bank_info(url,user_bank_type,i))
    for item in bank:
        print(item)
if __name__=="__main__":
    main()
