import requests
from lxml import etree
import json

class ZhilianSpider(object):

    def __init__(self):
        self.url = "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%b9%bf%e4%b8%9c&kw=Python&sm=0&sg=0ee3d6d3c4db4dee99815db2637bf2e7&p=1"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }

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

    def get_page_from_url(self, url):
        '''发送请求,获取页面数据'''
        response = requests.get(url, headers = self.headers)
        # print(response.content.decode())
        return response.content

    def get_data_from_page(self, page):
        element = etree.HTML(page)
        tables = element.xpath('//*[@id="newlist_list_content_table"]/table')

        data_list = []
        for table in tables:
            work = {}
            work["岗位"] = table.xpath('.//td[1]/div/a[1]/text()')
            work["公司名称"] = table.xpath('.//td[3]/a[1]/text()')
            work["职位月薪"] = table.xpath('.//td[4]/text()')
            work["工作地点"] = table.xpath('.//td[5]/text()')
            print(work)
            data_list.append(work)

        next_url = element.xpath('//a[text()="下一页"]/@href')
        next_url = next_url[0] if len(next_url) !=0 else None

        return data_list, next_url



    def save_data(self, data_list):
        '''保存数据'''
        with open("智联招聘岗位", "a", encoding="utf8") as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")


if __name__ == '__main__':

    job = ZhilianSpider()
    # print(requests.utils.unquote(job.url))
    job.run()