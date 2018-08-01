import requests

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36"
# }

headers ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

# response = requests.get("http://www.baidu.com", headers=headers)

# 发送带有请求头的请求
response = requests.get('http://www.baidu.com', headers=headers)

print(response.content.decode())