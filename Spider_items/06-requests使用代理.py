'''
格式:
proxies = {
"http": "http://username:password@ip:port"}
"https": "https://username:password@ip:port"}
response = requests.get(url, proxies=proxies)
'''
import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}

proxies = {
    "http": "http://121.8.98.198:80"
}

response = requests.get("http://www.baidu.com", headers=headers, proxies=proxies)

if __name__ == '__main__':
    print(response.content.decode())
