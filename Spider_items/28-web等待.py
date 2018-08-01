from selenium import webdriver
import time

# 创建浏览器的驱动
driver = webdriver.Chrome()

# 访问百度
driver.get("http://www.baidu.com")

# 定位元素
input_element = driver.find_element_by_id("kw")
# 搜索传智播客
input_element.send_keys("传智播客")
# 点击搜索
driver.find_element_by_id("su").click()

# driver只有在get的第一次请求才会等待加载完毕，js和点击按钮跳转页面可能找不到元素
# 等待有三种方式
# 1.强制等待
# time.sleep(3)

# 2.隐式等待：等待页面加载完成或者时间到了
driver.implicitly_wait(3)

# 3.显示等待:等待到满足某个条件时为止


# 点击下一页
driver.find_element_by_partial_link_text("下一页").click()

# 关闭浏览器
driver.quit()