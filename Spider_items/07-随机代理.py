'''
1.random.choice()
2.
'''
import requests
import random

# 准备代理池
proxies_list = [
    {'http': '106.112.161.242:808'},
    {'http': '43.229.88.98:53281'},
    {'http': '121.8.98.198:80'},
    {'http': '39.108.234.144:80'},
    {'http': '125.120.201.68:808'},
    {'http': '91.107.5.210:51816'},
    {'http': '103.28.149.180:3128'},
    {'http': '36.67.20.251:52136'},
    {'http': '116.90.225.154:53281'},
    {'http': '151.106.25.232:1080'},
]
'''
for i in range(10):
    # 在代理池中随机取一个代理
    proxies = random.choice(proxies_list)
    try:
        # 发起请求, 并指定超时参数
        response = requests.get("http://www.baidu.com", proxies=proxies, timeout=2)
        print(response.status_code)
    except Exception as e:
        print("代理{}不可用".format(proxies))
        # 如果代理不可用就从列表中删除
        proxies_list.remove(proxies)
'''

for proxies in proxies_list:
    try:
        # 发起请求, 并指定超时参数
        response = requests.get("http://www.baidu.com", proxies=proxies, timeout=2)
        print(response.status_code)
    except Exception as e:
        print("代理{}不可用".format(proxies))
        proxies_list.remove(proxies)
print(proxies_list)
