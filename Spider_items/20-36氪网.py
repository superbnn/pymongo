import requests
import re
import json


class ThirtyThreeKrSpider(object):
    '''获取36氪网的首页信息'''

    def __init__(self):
        # 准备url
        self.url = "http://36kr.com/"
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        }

    def get_page_from_url(self, url):
        '''发送请求,获取页面数据'''
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_data_from_page(self, page):
        '''分析数据,提取需要的内容'''
        # '<script>var props='
        json_str = re.findall(r'<script>var props=(.+?),locationnal=.*</script>', page)[0]
        # 当你去某一行某一列查找数据时,要把它写进文件
        # with open("36kr.test.json", "w", encoding="utf8") as f:
        #     f.write(json_str)
        json_dict = json.loads(json_str)
        return json_dict

    def save_data(self, data):
        '''保存数据'''
        with open("36kr.json", "w", encoding="utf8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def run(self):
        '''程序入口,主干逻辑'''
        # 1.发送请求,获取页面数据
        page = self.get_page_from_url(self.url)
        # 2.分析数据,提取需要的内容
        data = self.get_data_from_page(page)
        # 3.保存数据
        self.save_data(data)

if __name__ == '__main__':
    kr = ThirtyThreeKrSpider()
    kr.run()