import requests
'''爬取贴吧指定页数据'''


class TiebaSpider(object):
    '''定义一个贴吧爬虫类'''

    def __init__(self, name, start_page, end_page):
        self.name = name
        self.start_page = start_page
        self.end_page = end_page
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
        }
        self.url_pattern = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"

    def run(self):
        url_list = self.get_url_list()
        self.save_content(url_list)

    def get_url_list(self):
        # url_list = []
        # for i in range(self.start_page, self.end_page+1):
        #     url_list.append(self.url_pattern.format(self.name, (i-1)*50))
        # return url_list

        # 列表生成式
        return [self.url_pattern.format(self.name, (i - 1) * 50) for i in range(self.start_page, self.end_page + 1)]

    def save_content(self, url_list):
        '''保存提取的信息'''
        for url in url_list:
            response = requests.get(url, headers=self.headers)
            filename = "{}_第{}页.html".format(self.name, url_list.index(url)+1)
            with open(filename, "wb") as f:
                f.write(response.content)


if __name__ == '__main__':
    tb = TiebaSpider("三国杀", 1, 3)
    tb.run()
