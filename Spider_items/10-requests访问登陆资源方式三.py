'''
使用session进行登陆
'''
import requests

# 获取session对象,方法和requests一样
session = requests.session()

# 设置属性来设置请求头,每次使用该session对象发请求时都会携带该请求头
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400',
    # 'Cookie': 'anonymid=jhn8zwp8-96niy2; depovince=GW; _r01_=1; JSESSIONID=abctzKFvJQurk_lmI_Bow; ick_login=83072f58-0f29-4f59-bea0-305e8c358827; t=8f7c38132b035df2c1126906e529855e4; societyguester=8f7c38132b035df2c1126906e529855e4; id=966132334; xnsid=63b05894; jebecookies=894cf564-22ad-4e86-8caf-c8dbd2457e96|||||; jebe_key=270f4908-df6c-45c5-80a1-89ef841f62e5%7C8455dddaf9a4bb1c1ae351fb4adef1c7%7C1527335864207%7C1%7C1527335947082; XNESSESSIONID=8f97111197c7; ver=7.0; loginfrom=null; wp_fold=0'
}

# 登陆url和数据
url = "http://www.renren.com/PLogin.do"

data = {
    "email": 'lideshan12@163.com',
    'password':'A123456'
}

# 发起登陆请求
response = session.post(url, data=data)

with open("login.html", "wb") as f:
    f.write(response.content)

# 使用该session去访问登陆的资源
response = session.get("http://www.renren.com/965194180/profile")

with open("home.html", "wb") as f:
    f.write(response.content)

