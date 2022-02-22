# -*- coding = utf-8 -*-
# @Time : 2021/1/22 10:46
# @Author : xxx
# @File : requests爬豆瓣电影.py
# @Software : PyCharm

'''
   get请求
   返回json
'''
import requests
import json
if __name__ == '__main__':

    url = 'https://movie.douban.com/j/chart/top_list'

    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',  #从库中第几部电影中去取
        'limit': '20'   #一次取出的个数
    }

    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.141Safari / 537.36Edg / 87.0.664.75'
    }

    response = requests.get(url=url,params=param,headers=headers)

    list_obj = response.json()
    print(list_obj)

    # fp = open("豆瓣电影.json", 'w', encoding='utf-8')
    # json.dump(list_obj, fp=fp, ensure_ascii=False)  # 把dic_obj写入fp对象中，不使用ascii编码
    # fp.close()  # json打开后必须要关闭

    print("爬完了")