import json
import sys
import requests


class FanyiSpider(object):
    '''定义一个百度翻译爬虫类'''

    def __init__(self, word):
        self.word = word
        self.detect_url = "http://fanyi.baidu.com/langdetect"
        self.trans_url = "http://fanyi.baidu.com/basetrans"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"}

    def get_data_form_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return response.content.decode()

    def run(self):
        # 组织参数
        data = {
            "query": self.word
        }

        # 发送请求,获取响应数据
        result = self.get_data_form_url(self.detect_url, data)
        # 将json字符串转化为字典数据
        result_dict = json.loads(result)
        # print(result_dict)
        data["from"] = result_dict["lan"]
        # 格式: 结果1 if 条件 结果2
        # 条件成立:结果1  条件不成立:结果2
        data["to"] = "zh" if result_dict["lan"] == "en" else "en"
        # 发送请求,获取响应
        result = self.get_data_form_url(self.trans_url, data)
        # 将返回值转化为字典
        result_dict = json.loads(result)
        # print(result_dict['trans'][0]['dst'])
        print(result_dict['trans'][0]['dst'])

if __name__ == '__main__':
    # print(sys.argv)
    word = sys.argv[1]
    # word = input("请输入要翻译的单词:")
    demo = FanyiSpider(word)
    demo.run()