# -*- coding = utf-8 -*-
# @Time : 2021/1/22 10:01
# @Author : xxx
# @File : requests爬百度翻译.py
# @Software : PyCharm

'''
   携带了参数的post请求
   相应的数据是一组json数据
'''
import requests
import json
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'

    #post请求的参数(和get的param参数一样)
    kw = input("输入词 ：")
    data={
        'kw': kw
    }

    # 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.141Safari / 537.36Edg / 87.0.664.75'
    }

    response = requests.post(url=post_url,data=data)

    #获取相应数据json()返回的是字典对象（服务器相应的数据确认是json的才能用）
    dic_obj = response.json()

    #持久化存储
    flieName = './'+kw+'.json'  #存储路劲
    fp = open(flieName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)   #把dic_obj写入fp对象中，不使用ascii编码
    fp.close()   #json打开后必须要关闭

    print("爬完了")
