import requests

wd = input("请输入要查找的内容:")

headers ={
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}

# url = "http://www.baidu.com/s?wd={}"
# url = url.format(wd)

params = {
    "wd": wd
}

response = requests.get("http://www.baidu.com/s", params=params, headers=headers)

if __name__ == '__main__':

    print(response.content.decode())
