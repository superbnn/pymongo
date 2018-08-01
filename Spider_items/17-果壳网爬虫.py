import json
import re

import requests


class GuoKrSpider(object):
    '''爬取果壳网上精彩问答的地址和标题'''

    def __init__(self):
        # 准备url
        self.url = "https://www.guokr.com/ask/highlight/"
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        }

    def get_page_from_url(self, url):
        '''发起请求,获取响应'''
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_data_from_page(self, page):
        '''解析数据,提取需要的内容'''
        # '<h2><a target="_blank" href="https://www.guokr.com/question/669761/">印度人把男人的生殖器叫林伽，把女人的生殖器叫瑜尼，林伽和瑜尼的交合，便是瑜伽。这是真还是假的</a></h2>'
        data_list = re.findall(r'<h2><a target="_blank" href="(.+?)">(.+?)</a></h2>', page, re.S)
        return data_list

    def save_data(self, data_list):
        '''保存数据,一条问答保存一行'''
        for data in data_list:
            with open("guokr.json", "a", encoding="utf8") as f:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        '''程序入口,主干逻辑'''
        # 1.发送请求,获取页面数据
        page = self.get_page_from_url(self.url)
        # print(page)
        # 2.解析数据,提取需要的内容
        data_list = self.get_data_from_page(page)
        # print(data_list)
        # 3.保存数据,一条问答保存一行
        self.save_data(data_list)

if __name__ == '__main__':
    guokr = GuoKrSpider()
    guokr.run()