'''
方案2:
    我们可以从上一页的数据中,提取出来下一页URL
    1. 在解析数据的时候,提取下一页的URL
    2. 交给run方法
    3. 如果有下一页的URL就循环, 否则结束循环
'''
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
        # 下一页的url不完整,要进行拼接
        self.pre_url = "https://www.guokr.com"

    def get_page_from_url(self, url):
        '''发起请求,获取响应'''
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_data_from_page(self, page):
        '''解析数据,提取需要的内容'''
        # '<h2><a target="_blank" href="https://www.guokr.com/question/669761/">印度人把男人的生殖器叫林伽，把女人的生殖器叫瑜尼，林伽和瑜尼的交合，便是瑜伽。这是真还是假的</a></h2>'
        data_list = re.findall(r'<h2><a target="_blank" href="(.+?)">(.+?)</a></h2>', page, re.S)
        # '<a href="/ask/highlight/?page=100">下一页</a>'
        next_url = re.findall(r'<a href="(.+?)">下一页</a>', page)
        # 如果findall没有找到下一页,返回一个空列表
        next_url = self.pre_url + next_url[0] if len(next_url) != 0 else None
        return data_list, next_url

    def save_data(self, data_list):
        '''保存数据,一条问答保存一行'''
        for data in data_list:
            with open("guokr.json", "a", encoding="utf8") as f:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        '''程序入口,主干逻辑'''
        url = self.url
        while url is not None:
            # 1.发送请求,获取页面数据
            page = self.get_page_from_url(self.url)
            # print(page)
            # 2.解析数据,提取需要的内容
            data_list, url = self.get_data_from_page(page)
            # print(data_list)
            # 3.保存数据,一条问答保存一行
            self.save_data(data_list)

if __name__ == '__main__':
    guokr = GuoKrSpider()
    guokr.run()