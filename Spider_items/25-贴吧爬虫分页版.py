'''etree.HTML() 支持字节类型和没有xml声明的文本类型
所以如果文档中xml声明,如:<?xml version="1.0" encoding="UTF-8"?>, 就只能传入字节数据, 而不能传入字符串
'''
import json

import requests
from lxml import etree


class TiebaSpider(object):
    '''爬取某个贴吧所有的帖子,获取每个帖子的标题 链接和帖子中图片'''

    def __init__(self, tb_name):
        self.tb_name = tb_name
        # 准备url
        self.url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw={}&lp=9001".format(self.tb_name)
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Mobile Safari/537.36',
        }
        # url前缀
        self.pre_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"

    def get_page_from_url(self, url):
        '''发送请求,获取页面数据'''
        response = requests.get(url, headers = self.headers)
        return response.content

    def get_data_from_page(self, page):
        '''分析数据,提取需要的内容'''
        # 要解析的内容如果声明了编码方式,不能用字符串,要使用二进制
        element = etree.HTML(page)
        # print(etree.tostring(element).decode())
        # 先分组,获取所有的主题标签
        a_ls = element.xpath('//div[contains(@class, "i")]/a')
        # 创建列表，用于保存数据
        data_list = []

        # 遍历标签列表，保存标题和url
        for a in a_ls:
            item = {}
            item["title"] = a.xpath("./text()")[0]
            item["detail_url"] = self.pre_url + a.xpath("./@href")[0]
            data_list.append(item)

        next_url = element.xpath('//a[text()="下一页"]/@href')
        next_url = self.pre_url + next_url[0] if len(next_url) != 0 else None

        return data_list, next_url

    def save_data(self, data_list):
        '''保存数据'''
        with open("{}.json".format(self.tb_name), "a", encoding="utf8") as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        '''程序入口,主干逻辑'''
        url = self.url
        while url is not None:
            # 1.发送请求,获取页面数据
            page = self.get_page_from_url(url)
            # print(page.decode())
            # 2.分析数据,提取需要的内容
            data_list, url = self.get_data_from_page(page)
            # 3.保存数据
            self.save_data(data_list)

if __name__ == '__main__':
    tieba = TiebaSpider("李冰冰")
    tieba.run()