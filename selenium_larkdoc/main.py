from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import countdown

# 免登录步骤，将运行浏览器的数据文件（包含cookies）存储在指定文件夹，下次运行时可免登录
edge_options = webdriver.EdgeOptions()
edge_options.add_argument(r'--user-data-dir=D:\softwaredata\Edge_selenium')  # 设置用户文件夹，可免登陆
service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=edge_options)


def switch_to_window(driver, window_index):
    """切换到最新打开的窗口"""
    all_handles = driver.window_handles
    new_window_handle = all_handles[window_index]
    driver.switch_to.window(new_window_handle)

def click_element(element):
    """点击元素"""
    if element:
        first_element = element[0]
    first_element.click()

def open_new_webpage(driver, new_url):
    """打开新标签页"""
    driver.execute_script("window.open('', '_blank');")
    # 切换到新标签页
    driver.switch_to.window(driver.window_handles[-1])
    # 在新标签页中打开指定的URL
    driver.get(new_url)

# 主程序

driver.get('https://oa3czxzloyj.feishu.cn/drive/me/')
time.sleep(2)  # 需要根据实际页面加载时间调整等待时长

# 打开第二个网站并切换至新页面
open_new_webpage(driver, 'https://flowus.cn/')
time.sleep(2)  # 需要根据实际页面加载时间调整等待时长

switch_to_window(driver, 0)

# 设置过滤器为按名称排序
element = driver.find_elements(By.XPATH, '//button[@class="sc-gSQGeZ haNiFB"]')
click_element(element)
elements_2 = driver.find_elements(By.XPATH, '//div[@class="ud__text ud__menu-normal-item-title-content ud__menu-normal-item-title-content-text-overflow ud-typography-body-0 u14wgoeq u238cxi u1bdmrri uodcvno u11adn32 u1f3wrh8 uxkbsdt udz62fk u6rw91u u1urq0v1 uktmkt9"]')
click_element(elements_2)

# 定位文档列表（无文件夹）
elements = driver.find_elements(By.XPATH, '//li[@class="file-list-item"]') 

element_folders_root = driver.find_elements(By.XPATH, '//ul[@class="sc-jUotMc eFNjah" and @data-e2e="folder-sm-grid-list"] /child::div')

# 索引文件夹中的每个文档
#for i in range(len(element_folders_root)):
    # 进入第一个文件夹
#    element_folders_root[i].click()

#    elements_1 = driver.find_elements(By.XPATH, '//li[@role="item" and @class="file-list-item"]') 
#    for j in range(len(elements_1)):
    

# 循环根文件夹下的文档
for i in range(len(elements)):
    # 切换窗口至原页面（feishu）
    switch_to_window(driver, 0)

    # 点击第 i 个文档
    elements[i].click()

    # 等待新页面加载
    time.sleep(2)  # 需要根据实际页面加载时间调整等待时长

    # 切换窗口至新打开的页面（feishu）
    switch_to_window(driver,-1)

    # 点击标题
    elements_inside = driver.find_elements(By.XPATH, '//div[@class="page-block-content left flash-block-content"]')
    click_element(elements_inside)

    # 全选、复制
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(0.5)  # 等待选中
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

    # 切换窗口至页面（flowus）
    switch_to_window(driver, 1)

    # 点击新建文件
    elements_inside  = driver.find_elements(By.XPATH, '//button[@class="rounded-sm cursor-pointer animate-hover"]')
    click_element(elements_inside)
    time.sleep(0.5)  

    # 粘贴
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    # 切换窗口至feishu
    switch_to_window(driver, -1)

    # 点击第一行（选中文本）
    elements_inside = driver.find_elements(By.CLASS_NAME, 'render-unit-wrapper')
    click_element(elements_inside)

    # 全选、复制
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').send_keys('a').send_keys('a').key_up(Keys.CONTROL).perform()
    time.sleep(0.5)  # 等待选中
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    

    # 切换窗口至页面（flowus）
    switch_to_window(driver, 1)

    webdriver.ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    # 点击新建类型为文档
    #elements_inside  = driver.find_elements(By.XPATH, '//div[@class="line-default text-grey4"]/child::div[2]')
    #click_element(elements_inside)
    
    # 点击选择文档编辑区第一行（必要且重要）
    elements_inside  = driver.find_elements(By.XPATH, '//div[@class="px-0.5 py-1 text-t1 group"]')
    click_element(elements_inside)

    # 粘贴
    webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)  

    # 关闭第二个网站
    switch_to_window(driver, -1)
    driver.close()

# 关闭浏览器
driver.quit()
