import requests
import json
import js2py


class RRLoginSpider(object):
    '''人人网手机端登陆'''

    def __init__(self):
        # 登陆url
        self.clog_url = 'http://activity.renren.com/livecell/ajax/clog'
        # rekyURL
        self.rkey_url = 'http://activity.renren.com/livecell/rKey'
        self.session = requests.session()
        # 请求头
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
        }


        # 创建js执行环境
        self.context = js2py.EvalJs()

    def get_data_from_url(self, url, data=None):
        '''根据url返回对应数据'''
        if data is None:
            '''没有数据,发送get请求'''
            response = self.session.get(url)
        else:
            response = self.session.post(url, data=data)

        # 返回二进制响应数据
        return response.content

    def load_js_from_url(self, url):
        '''根据Url让js环境去加载js'''
        js = self.get_data_from_url(url).decode()
        self.context.execute(js)

    def run(self):
        '''程序入口,主干逻辑'''
        # 发起get请求,获得响应数据
        rkey_json = self.get_data_from_url(self.rkey_url)
        # 解析获取json数据,赋值给n
        n = json.loads(rkey_json.decode())['data']

        # 向执行环境中添加数据
        self.context.t = {
            'phoneNum':'15565280933',
            'password': 'a123456',
            'c1': 0
        }

        self.context.n = n

        # 让js执行环境去加载需要的js
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js")
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js")
        self.load_js_from_url("http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js")

        # 加密密码js
        js = '''
            t.password = t.password.split("").reverse().join(""),
            setMaxDigits(130);
            var o = new RSAKeyPair(n.e,"",n.n)
            , r = encryptedString(o, t.password);
            t.password = r,
            t.rKey = n.rkey
             '''

        # 执行js,执行后执行环境中t就是登陆请求中的数据
        self.context.execute(js)
        print(self.context.t)
        # print(type(self.context.t))
        # 获取某个对象有哪些方法
        # print(dir(self.context.t))

        # 发送登陆请求,获取登陆后的数据
        # result = self.session.post(self.clog_url, data=self.context.t.to_dict())
        result = self.get_data_from_url(self.clog_url, self.context.t.to_dict())
        print(json.loads(result.decode()))

        # 使用登陆后的session访问登陆后的资源
        # response = self.session.get('http://activity.renren.com/myprofile')
        url = 'http://activity.renren.com/myprofile'
        response = self.get_data_from_url(url)

        with open("home2.html", "wb") as f:
            f.write(response)


if __name__ == '__main__':
    rrs = RRLoginSpider()
    rrs.run()
