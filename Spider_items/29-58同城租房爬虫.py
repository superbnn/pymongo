import json

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class ZuFangSpider(object):
    '''爬取租房信息的爬虫'''

    def __init__(self):
        # 创建配置选项的对象
        op = Options()
        op.set_headless()

        # 创建浏览器的驱动
        self.driver = webdriver.Chrome(options=op)

        # 请求租房的首页
        self.driver.get("http://sz.58.com/chuzu/")

    def __del__(self):
        '''对象被销毁的时候调用'''
        # self.driver.quit()
        pass

    def get_data(self):
        '''通过driver对象，解析内容，获取需要的内容'''
        # 定位元素，获取标签分组 最后混进了奇怪的li标签，需要进行过滤，-1或者-2都行
        li_list = self.driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div[5]/div[2]/ul/li')[:-2]
        print(len(li_list))

        # 定义一个列表保存数据
        data_list =[]

        # 遍历标签列表，提取需要的数据
        for li in li_list:
            item = {}
            # 过滤掉广告的标签
            if li.get_attribute("class") == 'apartments-pkg apartments':
                # 跳过本次循环下面的语句，继续下一次循环
                continue

            # 获取图片url，标题，详情url，价格
            item["img_url"] = li.find_element_by_xpath('./div[1]/a/img').get_attribute("src")
            item["title"] = li.find_element_by_xpath('./div[2]/h2/a').text
            item["detail_url"] = li.find_element_by_xpath('./div[2]/h2/a').get_attribute("href")
            item["price"] = li.find_element_by_xpath('./div[3]/div[2]/b').text
            data_list.append(item)
            # print(item)
        print(len(data_list))

        # 获取下一页的按钮:使用find_elements，因为最后一页没有下一页，我们不想程序找不到报错而终止运行
        next_page = self.driver.find_elements_by_class_name("next")
        next_page = next_page[0] if len(next_page) != 0 else None

        return data_list, next_page

    def save_data(self, data_list):
        '''保存数据'''
        with open("58同城租房.txt", "a", encoding="utf8") as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        '''程序入口，主干逻辑'''
        data_list, next_page = self.get_data()

        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    zufang = ZuFangSpider()
    zufang.run()