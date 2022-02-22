# -*- coding = utf-8 -*-
# @Time : 2021/1/22 9:14
# @Author : xxx
# @File : requests爬搜狗.py
# @Software : PyCharm

import requests

if __name__ == '__main__':
    # 1.指定url
    url = "https://www.sogou.com/"

    # 2.发起请求
    response = requests.get(url=url)  # get方法会返回一个相应对象

    # 3.获取响应数据(html页面)(字符串形式)
    page_text = response.text

    # 4.持久化存储
    with open('./sougou.html', "w", encoding="utf-8") as fp:   #文件名为./sougou.html，写入方式为w，格式为utf-8，写入page_text
        fp.write(page_text)

    print("爬完了")
