# -*- coding = utf-8 -*-
# @Time : 2021/1/22 9:36
# @Author : xxx
# @File : resuests爬网页采集器.py
# @Software : PyCharm


#UA：user-Agent(请求载体的身份标识)
#UA检查：网址服务器会检查UA，如果UA是浏览器，则可以正常浏览，否则不让浏览
#UA伪装：UA伪装成浏览器
'''
get请求
返回text
'''
import requests

if __name__ == '__main__':

    url = "https://www.sogou.com/web"

    # 处理url的参数:封装到字典中
    kw = input("输入关键词 ：")
    param = {
        "query": kw
    }

    #进行UA伪装  将UA封装到一个字典中   可以多弄几个浏览器的UA然后用random调用
    headers = {
        'User-Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.141Safari / 537.36Edg / 87.0.664.75'
    }

    #对指定的url发起的请求对应的url是携带参数的，并在请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)

    page_text = response.text

    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName,"爬完了")