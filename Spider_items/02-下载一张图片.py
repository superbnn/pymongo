import requests

headers ={
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}

response = requests.get("https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3198611610,3108821463&fm=27&gp=0.jpg")

if __name__ == '__main__':
    with open("b.jpg", "wb") as file:
        file.write(response.content)