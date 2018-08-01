'''
需求：爬取斗鱼直播房间图片，房间url，房间标题，房间类别，房间所有者，房间热度信息
'''
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json
import time


class DouYuSpider(object):
    '''爬取斗鱼直播信息爬虫'''

    def __init__(self):

        # 设置无界面浏览器
        op = Options()
        op.set_headless()

        self.driver = webdriver.Chrome(options=op)

        # 访问斗鱼直播页面内容
        self.driver.get("https://www.douyu.com/directory/all")

        # 房间地址前缀
        self.pre_url = "https://www.douyu.com"

    def get_data(self):
        '''获取页面数据'''
        # 定位元素，获取标签分组
        li_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')

        # 定义列表，保存数据
        data_list = []

        # 遍历标签
        for li in li_list:
            item = {}
            try:
                item["room_img"] = li.find_element_by_xpath('./a/span/img').get_attribute("src")
                item["room_url"] = self.pre_url + li.find_element_by_xpath('./a').get_attribute("href")
                item["room_title"] = li.find_element_by_xpath('./a/div/div/h3').text
                item["room_category"] = li.find_element_by_xpath('./a/div/div/span').text
                item["room_author"] = li.find_element_by_xpath('./a/div/p/span[1]').text
                item["room_hot"] = li.find_element_by_xpath('./a/div/p/span[2]').text
                print(item)
            except Exception as e:
                '''在真实开发中，所有异常都要处理，记录在日志中，如果错误比较严重，可以让程序自动发邮件给你'''
                print(e)
            data_list.append(item)

        # todo:获取下一页按钮:为了防止最后一页没有下一页按钮报错，采用find_elements
        next_page = self.driver.find_elements_by_class_name("shark-pager-next")
        next_page = next_page[0] if len(next_page) != 0 else None

        return data_list, next_page

    def save_data(self, data_list):
        '''保存数据'''
        with open("斗鱼直播爬虫.txt", "a", encoding="utf8") as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")

    def run(self):
        '''程序入口，主干逻辑'''
        while True:
            # 1.获取直播房间信息
            data_list, next_page = self.get_data()

            # 2.保存数据
            self.save_data(data_list)

            # 判断是否有下一页数据
            if next_page is not None:
                next_page.click()
                print("下一页")
                # 当页面使用js动态生成，只能用强制等待
                time.sleep(3)
            else:
                break

        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    douyu = DouYuSpider()
    douyu.run()