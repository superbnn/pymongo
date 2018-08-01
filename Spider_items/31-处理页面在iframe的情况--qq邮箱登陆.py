from selenium import webdriver
import time

# 创建浏览器驱动
driver = webdriver.Chrome()

# 访问qq邮箱登录页
driver.get("https://mail.qq.com/")

# 每一个Iframe是一个独立页面，driver访不能直接访问，需要切换到这个页面
driver.switch_to.frame('login_frame')
"""
        Switches focus to the specified frame, by index, name, or webelement.

        :Args:
         - frame_reference: The name of the window to switch to, an integer representing the index,
                            or a webelement that is an (i)frame to switch to.

        :Usage:
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        """

# 找到用户输入框，输入用户
driver.find_element_by_id('u').send_keys("deshanlee@qq.com")

# 找到密码输入框，输入密码
driver.find_element_by_id("p").send_keys("lw19860404")

# 找到登陆按钮
driver.find_element_by_id("login_button").click()


time.sleep(3)

# 关闭浏览器
driver.quit()