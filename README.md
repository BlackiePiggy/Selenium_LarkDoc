# Selenium_LarkDoc

- 进入主页面
一个完整循环
- 点击第一个文档，并切换至打开的文档窗口
elements = driver.find_elements(By.CLASS_NAME, 'file-list-item')  # 替换 'element_x' 为实际的选择器
    if i < len(elements):
        elements[i].click()
        
        # 等待新页面加载
        time.sleep(5)  # 需要根据实际页面加载时间调整等待时长

        # 获取所有窗口句柄
        all_handles = driver.window_handles

        # 切换到新窗口
        new_window_handle = all_handles[-1]
        driver.switch_to.window(new_window_handle)
- 单击第一行，全选复制
[图片]
        #选中第一行
        elements_inside = driver.find_elements(By.CLASS_NAME, 'text-block-wrapper')

        if elements_inside:
            first_element = elements_inside[0]

        first_element.click()

        # 执行 Ctrl+A 和 Ctrl+C
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(1)  # 等待选中
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
- 切换至flowus页面
        # 获取所有窗口句柄
        all_handles = driver.window_handles

        # 切换到新窗口
        new_window_handle = all_handles[-1]
        driver.switch_to.window(new_window_handle)
- 选择新建文档按钮，点击
        elements_inside  = driver.find_elements(By.XPATH, '//button[@class="rounded-sm cursor-pointer animate-hover"]')
        if elements_inside:
            first_element = elements_inside[0]

        first_element.click()
- 选择新建类型为页面，点击
        elements_inside  = driver.find_elements(By.XPATH, '//div[@class="flex items-center p-1 h-9 animate-hover"]')
        if elements_inside:
            first_element = elements_inside[0]
        first_element.click()
- 选择第一行，点击（这一步必不可少）
        elements_inside  = driver.find_elements(By.XPATH, '//div[@class="px-0.5 py-1 text-t1 group"]')
        if elements_inside:
            first_element = elements_inside[0]
        first_element.click()
- 粘贴
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
