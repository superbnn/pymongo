'''
url对应的图片不变，直接请求
url对应的图片是变化的，需要在请求时携带cookie信息
判断是否有验证码时，用find_elements，即使没有不会报错
'''
from selenium import webdriver
import requests
import yudama
import time

# 创建驱动
# from yudama import indetify

driver = webdriver.Chrome()

# 访问豆瓣首页
driver.get("https://www.douban.com/")

# 找到用户名输入框，输入用户
driver.find_element_by_id('form_email').send_keys("583349285@qq.com")
# 找到密码输入框，输入密码
driver.find_element_by_id("form_password").send_keys("lw19860404")

# 识别验证码
# 1.url对应的图片不变，直接请求
# 2.url对应的图片变化，请求时要携带cookie信息
# 判断是否有验证码，没有，不报错
img_element = driver.find_elements_by_id("captcha_image")
if len(img_element) != 0:
    # 获取图片响应
    img_url = img_element[0].get_attribute("src")
    response = requests.get(img_url)

    # 通过云打码平台，识别图片验证码
    code = yudama.indetify(response.content)

    # 获取验证码输入框，输入验证码
    driver.find_element_by_id("captcha_field").send_keys(code)

    time.sleep(5)

# 点击登陆按钮，进行登陆
driver.find_element_by_class_name('bn-submit').click()


time.sleep(10)
# 关闭驱动
driver.quit()
