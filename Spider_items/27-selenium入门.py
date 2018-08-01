from selenium import webdriver
import time

# 无界面浏览器实现
from selenium.webdriver.chrome.options import Options
op = Options()
op.set_headless()
# 创建chrome浏览器的驱动
driver = webdriver.Chrome(options=op)

# 加载网页（访问百度首页）
# driver.get("http://www.baidu.com")
driver.get('http://www.baidu.com')

# 定位元素
# 根据id定位元素
# input_element = driver.find_element_by_id("kw")
# 根据name属性定位元素
# input_element = driver.find_element_by_name("wd")
# 根据xpath定位元素
input_element = driver.find_element_by_xpath('//*[@id="kw"]')
# 根据文本获取标签
hao123 = driver.find_element_by_link_text("hao123")
# 根据部分文本获取标签
# hao123 = driver.find_element_by_partial_link_text("hao")
#u1 > a:nth-child(2)
# 根据selector进行定位
# hao123 = driver.find_element_by_css_selector('#u1 > a:nth-child(2)')
# 获取多个元素 find_elements:找不到返回一个空列表

# 操作元素
# 给输入框设置内容
input_element.send_keys("python")
# 获取属性
# print(hao123.get_attribute('href'))
# 获取文本
# print(hao123.text)

# 打印当前的url
# print(driver.current_url)
# 保存快照
# driver.save_screenshot("baidu.png")

# 查看请求信息
# print(driver.page_source)
# print(driver.get_cookies())

# 等待
time.sleep(3)

# 退出
# 退出当前页面，若只有一页，退出浏览器
# driver.close()
# 退出浏览器
driver.quit()