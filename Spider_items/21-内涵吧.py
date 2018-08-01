import requests
import re
import json


class NeiHanDuanZiSpider(object):
    '''爬取内涵段子'''

    def __init__(self):
        self.url = "http://www.neihanpa.com/article/list_5_1.html"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        }

    def get_page_from_url(self, url):
        '''发送请求,读取页面数据'''
        response = requests.get(url, headers=self.headers)
        # todo:确定解码方式
        return response.content.decode("gbk")

    def get_data_from_page(self, page):
        '''分析数据,提取需要的内容'''
        '''
        <div class="f18 mb20">
                            <p>
	　　老师:“小明，你的梦想是什么？”小明沉思片刻道:“有房有铺，自己当老板，<br>
	妻子貌美如花，还有当官的兄弟” 老师:北宋有个人和你一样，他姓武！</p>
        </div>
        '''
        dz_list = re.findall(r'<div class="f18 mb20">(.+?)</div>', page, re.S)
        for dz in dz_list:
            # 获取段子在列表中索引
            index = dz_list.index(dz)
            # 注意,字符串为不可变类型,所以更改后需要重新赋值
            # 删除 <.*>|\s
            dz = re.sub(r'<.*>|\s', "", dz)
            # &ldquo; 或 &rdquo; 替换为 "
            dz = re.sub(r'&ldquo;|&rdquo;', '"', dz)
            # &hellip; 替换为 …
            dz = re.sub(r'&hellip;', '...', dz)
            dz_list[index] = dz
        # print(dz_list)
        return dz_list

    def save_data(self, dz_list):
        '''保存数据'''
        with open("neihanba.json", "a", encoding="utf8") as f:
            for dz in dz_list:
                json.dump(dz, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        '''程序入口,主干逻辑'''
        # 1.发送请求,读取页面数据
        page = self.get_page_from_url(self.url)
        # 2.分析数据,提取需要的内容
        dz_list = self.get_data_from_page(page)
        # 3.保存数据
        self.save_data(dz_list)

if __name__ == '__main__':
    neihan = NeiHanDuanZiSpider()
    neihan.run()