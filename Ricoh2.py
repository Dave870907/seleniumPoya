from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Ricoh2(name, driver):
    c = []
    # 前往192.168.2.6
    driver.get('http://192.168.2.6/web/guest/tw/websys/webArch/mainFrame.cgi')
    sleep(2)
    # 登入
    try:
        iframe = driver.find_element_by_css_selector('html > frameset > frame:nth-child(1)')
    except:
        driver.close()
        c.append('192.168.2.6 異常')
        return c
    driver.switch_to.frame(iframe)
    elem_enter = driver.find_element_by_css_selector('#rightAreaBox > div.contentsIconArea.clear > ul > li:nth-child(3) > a > span').click()

    # 登入使用者名稱
    b = driver.find_element_by_css_selector(
    " table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]:nth-child(1)")
    b.clear()
    b.send_keys("admin")
    # 登入
    elem_login = driver.find_element_by_css_selector("body > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(6) > td:nth-child(2) > input[type=submit]").click()

    # 裝置管理,通訊錄
    iframe1 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe1)
    elem_manage = driver.find_element_by_css_selector("#sectionLinks > ul > li:nth-child(2) > div > a > span.menuText").click()
    elem_address = driver.find_element_by_css_selector("#sectionLinks > ul > li:nth-child(2) > ul > li:nth-child(2) > a").click()
    
    # 登出
    def logout(driver):
        driver.switch_to.parent_frame()
        iframe = driver.find_element_by_css_selector('html > frameset > frame:nth-child(1)')
        driver.switch_to.frame(iframe)
        driver.find_element_by_css_selector('#rightAreaBox > div.contentsIconArea.clear > ul > li:nth-child(4) > a > span').click()
    
    # 有人正在操作的話(點擊下一頁)
    def nextpage(driver, element_object):
        sum = 0
        while 1:           
            try:
                element_object.click()
                print(sum)
                break
            except:
                sum += 1
                sleep(1)
                if sum >= 5:
                    c.append("192.168.2.6:使用者存取數量過多,請手動設定或有人正在操作")
                    logout(driver)
                    driver.close()
                    return c

    # 點選新增使用者
    driver.switch_to.default_content()
    iframe2 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe2)
    while 1:
        try:
            driver.execute_script('javascript:AddUser()')
            break
        except:
            sleep(1)
    # 勾選使用者驗證
    sum = 0
    while 1:
        try:
            # driver.switch_to.default_content()
            driver.switch_to.parent_frame()
            iframe3 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
            driver.switch_to.frame(iframe3)
            element_cert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div/div[2]/div[2]/div/form/ul[3]/li/div/dl/dt/label")))
            element_cert.click()
            #elem_cert = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[2]/div/form/ul[3]/li/div/dl/dt/label").click()
            print(sum)
            break
        except:
            sum += 1
            if sum >= 5:
                c.append("192.168.2.6:使用者存取數量過多,請手動設定或有人正在操作")
                logout(driver)
                driver.close()
                return c
            sleep(1)

    # 前往下一頁
    elem_next = driver.find_element_by_css_selector("#forwardButton > input")
    nextpage(driver, elem_next)

    # step 1 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe4 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe4)
    elem_name = driver.find_element_by_css_selector("#frame_main-mdl > div > ul > li:nth-child(2) > div > dl > dd > input")
    elem_name.clear()
    elem_name.send_keys(name)
    
    # 前往下一頁
    elem_n = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div[2]/div/ul/li[2]/input")
    nextpage(driver, elem_n)
    

    # step 2 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe5 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe5)
    sum = 0
    while 1:
        try:
            # elem_name1 = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/form/div/div/ul/li[1]/div/dl/dd/input")
            print(sum)
            elem_name1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[3]/div/div[6]/form/div/div/ul/li[1]/div/dl/dd/input")))
            elem_name1.send_keys(name)
            break
        except:
            sum += 1
            sleep(1)
            if sum >= 5:
                c.append("192.168.2.6:使用者存取數量過多,請手動設定或有人正在操作")
                logout(driver)
                driver.close()
                return c
    # 下一步
    elem_next = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/div[2]/div/ul/li[2]/input")
    nextpage(driver, elem_next)

    # 送出表單
    try:
        # 新增等待三秒 避免網頁等太久
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[7]/div[3]/div/ul/li[2]/input").click()
    except:
        # 資料已存在
        logout(driver)
        c.append('192.168.2.6已存在' + name)
        driver.close()
        return c
    
    try:
        elem_error = driver.find_element_by_xpath('/html/body/div/div[3]/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td/form[1]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td').click()
        c.append("192.168.2.6:使用者存取數量過多,請手動設定或有人正在操作")
        logout(driver)
        driver.close()
        return c
    except:
        # 登出
        logout(driver)
        c.append("成功輸入:192.168.2.6")
        driver.close()
        return c
