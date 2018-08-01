import requests
# 1.把cookie对象转化为字典

url = "http://www.baidu.com"

response = requests.get(url)

print(response.cookies)

dict = requests.utils.dict_from_cookiejar(response.cookies)

print(dict)


# 2.设置请求的超时时间 timeout=2
try:
    url = 'http://www.youtube.com'
    response = requests.get(url, timeout=3)
except Exception as e:
    print("连接超时")

# 3.url解码和编码
url = "https://www.baidu.com/s?word=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2"
print(requests.utils.unquote(url))

url_str = "https://www.baidu.com/s?word=传智播客"
print(requests.utils.quote(url_str))


# 4.请求SSL证书验证
# 发送HTTPS的请求,requests模块中本来就有信任的证书
# 有些网站的证书是自己生成的,requests模块中没有
url = "https://www.12306.cn/mormhweb/"

response = requests.get(url, verify=False)
print(response.content.decode())