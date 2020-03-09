from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def printerall (name, num, driver):
    driver.get('http://192.168.2.2/')
    #2020/3/9新增(進入被阻擋的連線)
    advanced = driver.find_element_by_css_selector('#details-button')
    advanced.click()
    proceed = driver.find_element_by_css_selector('#proceed-link')
    proceed.click()
    #-----------
    frame = driver.find_element_by_xpath('/html/frameset/frame')
    driver.switch_to.frame(frame)
    elem_1 = driver.find_element_by_css_selector('#documentColor')
    elem_1.click()
    elem_2 = driver.find_element_by_xpath('/html/body/form/div/div[3]/div[2]/div[1]/div/div/div[17]/table/tbody/tr/td[2]/div/div[2]/u/a/span')
    elem_2.click()
    # 20191112 網頁出來速度太慢 修改完成 by 柯 --下--
    """
    # 原本程式碼
    for i in range(0,5):
        sleep(1)
        print('我睡著了')
    print('我醒了喔!!!')
    """
    while 1:
        try:
            frame2 = driver.find_element_by_id('printingjobs')
            # 此處不可太早切換
            driver.switch_to.frame(frame2)
            elem_3 = driver.find_element_by_css_selector('#contentrowtable > tbody > tr:nth-child(1) > td:nth-child(6)')
            elem_3.click()
            break
        except:
            # 切回原本frame
            driver.switch_to.frame(frame)
            sleep(1)
    # 20191112 網頁出來速度太慢 修改完成 by 柯 --上--

    for i in range(0, 5):
        sleep(1)
        print('我睡著了')
    print('我醒了喔!!!')

    driver.switch_to.parent_frame()
    frame3 = driver.find_element_by_id("alphardmaedasboxadd")
    driver.switch_to.frame(frame3)
    elem_4 = driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr/td/div/table[2]/tbody/tr[3]/td[2]/input')

    elem_4.clear()
    elem_4.send_keys(num)
    elem_5 = driver.find_element_by_css_selector('#w300px')
    elem_5.clear()
    elem_5.send_keys(name)

    elem_open = driver.find_element_by_css_selector(
        '#outerdiv > table:nth-child(2) > tbody > tr:nth-child(15) > td:nth-child(2) > label:nth-child(1) > input[type=radio]')
    elem_open.click()
    driver.implicitly_wait(20)

    elem_del = driver.find_element_by_css_selector(
        '#outerdiv > table:nth-child(2) > tbody > tr:nth-child(20) > td:nth-child(2) > label:nth-child(1) > input[type=radio]')
    # elem_del.location_once_scrolled_into_view
    elem_del.click()
    elem_days = driver.find_element_by_xpath(
        '/html/body/form/div/table/tbody/tr/td/div/table[2]/tbody/tr[16]/td[2]/input')
    elem_days.clear()
    elem_days.send_keys('1')

    # elem_submit = driver.find_element_by_xpath('//*[@id="submit"]')
    
    elem_submit = driver.find_element_by_name('submit001')
    elem_submit.click()
    sleep(3)
    c = []
    # 判斷成功與否待修改
    try:
        driver.switch_to_alert().accept()
    except:
        c.append('成功輸入:192.168.2.2')
        return printer2(name, num, driver, c)
    # print("192.168.2.2已存在", name)
    c.append("192.168.2.2已存在" + name)
    return printer2(name, num, driver, c)
    
def printer2(name, num, driver, c):
    driver.get('http://192.168.2.190/')
    frame = driver.find_element_by_xpath('/html/frameset/frame')
    driver.switch_to.frame(frame)
    
    elem_1 = driver.find_element_by_xpath('//*[@id="tm3"]/div[1]')
    elem_1.click()

    elem_2 = driver.find_element_by_xpath('//*[@id="s6"]')
    elem_2.click()

    def test(driver):
        while 1:
            try:
                frame2 = driver.find_element_by_xpath('//*[@id="printingjobs"]')
                driver.switch_to.frame(frame2)
                elem_3 = driver.find_element_by_css_selector('#contentrowtable > tbody > tr:nth-child(1) > td:nth-child(6)')
                elem_3.click()
                # 加入等待三秒避免等待太久
                driver.implicitly_wait(3)
                break
            except:
                # 切回原本frame
                driver.switch_to.parent_frame()
                sleep(1)
    test(driver)
    while 1:
        try:
            driver.switch_to.parent_frame()
            frame3 = driver.find_element_by_id("alphardmaedasboxadd")
            driver.switch_to.frame(frame3)
            break
        except:
            test(driver)
    # 此處不穩定 待修改
    elem_4 = driver.find_element_by_css_selector('#outerdiv > table:nth-child(2) > tbody > tr:nth-child(3) > td.style194 > input')
    elem_4.clear()
    elem_4.send_keys(num)
    elem_5 = driver.find_element_by_css_selector('#w300px')
    elem_5.clear()
    elem_5.send_keys(name)
    elem_open = driver.find_element_by_css_selector('#outerdiv > table:nth-child(2) > tbody > tr:nth-child(15) > td.style194 > label:nth-child(1) > input[type=radio]')
    elem_open.click()
    # driver.implicitly_wait(20)

    elem_del = driver.find_element_by_css_selector('#outerdiv > table:nth-child(2) > tbody > tr:nth-child(20) > td.style194 > label:nth-child(1) > input[type=radio]')
    # elem_del.location_once_scrolled_into_view
    elem_del.click()
    elem_days = driver.find_element_by_css_selector('#outerdiv > table:nth-child(2) > tbody > tr:nth-child(16) > td.style194 > input')
    elem_days.clear()
    elem_days.send_keys('1')

    # elem_submit = driver.find_element_by_xpath('//*[@id="submit"]')
    # 20191114 by 柯
    '''
    try:
        elem_submit = driver.find_element_by_name('submit001')
        sleep(3)
        elem_submit.click()
        c.append('成功輸入:192.168.2.190')
        return printer3(name, num, driver, c)
    except UnexpectedAlertPresentException:
        c.append("192.168.2.190已存在" + name)
        return printer3(name, num, driver, c)
    '''
    elem_submit = driver.find_element_by_name('submit001')
    elem_submit.click()
    while 1:
        try:
            alert_text = driver.switch_to.alert.text
            driver.switch_to_alert().accept()
            break
        except:
            sleep(1)
    # print('print:', alert_text)
    if alert_text == '此號碼已登錄。':
        c.append("192.168.2.190已存在" + name)
    else:
        c.append('成功輸入:192.168.2.190')
    return printer3(name, num, driver, c)
    # 20191114

def printer3(name, num, driver, c):
    driver.get('https://192.168.231.2/')
    #2020/3/9新增(進入被阻擋的連線)
    advanced = driver.find_element_by_css_selector('#details-button')
    advanced.click()
    proceed = driver.find_element_by_css_selector('#proceed-link')
    proceed.click()
    #-----------
    frame = driver.find_element_by_xpath('/html/frameset/frame')
    driver.switch_to.frame(frame)
    # driver.implicitly_wait(20)
    elem_1 = driver.find_element_by_xpath('//*[@id="tm3"]/div[1]')
    elem_1.click()

    elem_2 = driver.find_element_by_xpath('//*[@id="s6"]')
    elem_2.click()


    # 新增按鍵
    '''try
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#subHeaderFixed > div.toolbar-container.wp100 > div:nth-child(1)')))
        element.click()
    finally:
        sleep(2):'''
    while 1:
        try:
            frame2 = driver.find_element_by_xpath('//*[@id="printingjobs"]')
            driver.switch_to.frame(frame2)
            element = driver.find_element_by_css_selector('#subHeaderFixed > div.toolbar-container.wp100 > div:nth-child(1)')
            element.click()
            break
        except:
            # driver.switch_to.frame(frame)
            driver.switch_to.parent_frame()
            sleep(1)
    #elem_3 = driver.find_element_by_css_selector('#subHeaderFixed > div.toolbar-container.wp100 > div:nth-child(1)')
    #elem_3.click()
    driver.switch_to.parent_frame()
    frame3 = driver.find_element_by_id("alphardmaedasabadd")
    driver.switch_to.frame(frame3)

    # 輸入編號
    elem_4 = driver.find_element_by_css_selector(
        '#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.style194 > input')
    elem_4.clear()
    elem_4.send_keys(num)

    # 輸入名稱
    elem_5 = driver.find_element_by_css_selector('#w300px')
    elem_5.clear()
    elem_5.send_keys(name)

    # 開啟文件刪除
    elem_open = driver.find_element_by_css_selector(
        '#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(13) > td.style194 > div')
    elem_open.click()
    driver.implicitly_wait(20)

    # 開啟列印後刪除
    elem_del = driver.find_element_by_css_selector('#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(18) > td.style194 > div')

    # 畫面拉到下面才找的到因素
    elem_del.location_once_scrolled_into_view
    elem_del.click()

    # 輸入天數
    elem_days = driver.find_element_by_css_selector(
        '#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(14) > td.style194 > input')
    elem_days.clear()
    elem_days.send_keys('1')
    
    
    # 20191114 by 柯
    '''
    while 1:
        try:
            # 點擊提交
            elem_submit = driver.find_element_by_css_selector('#footerFixed > div > div.wrap.right > input[type=submit]:nth-child(1)')
            elem_submit.click()
            c.append('成功輸入:192.168.231.2')
            break
        # 抓跳出的重複訊息
        except UnexpectedAlertPresentException:
            c.append("192.168.231.2已存在"+ name)
            driver.switch_to.alert.accept()
            return Ricoh(name, driver, c)
        except:
            sleep(1)
    # driver.switch_to.parent_frame()
    while 1:
        try:
            driver.switch_to.alert.accept()
            break
        except:
            sleep(1)
    '''
    # 點擊提交
    elem_submit = driver.find_element_by_css_selector('#footerFixed > div > div.wrap.right > input[type=submit]:nth-child(1)')
    elem_submit.click()
    while 1:
        try:
            alert_text = driver.switch_to.alert.text
            driver.switch_to_alert().accept()
            break
        except:
            sleep(1)
    # print('print:', alert_text)
    if alert_text == '此號碼已登錄。':
        c.append("192.168.231.2已存在"+ name)
    else:
        c.append('成功輸入:192.168.231.2')
    return Ricoh(name, driver,c)
    # 20191114

def Ricoh(name, driver, c):
    driver.get('http://192.168.231.1/web/guest/tw/websys/webArch/mainFrame.cgi')

    # 登入
    iframe = driver.find_element_by_css_selector('html > frameset > frame:nth-child(1)')
    driver.switch_to.frame(iframe)
    elem_enter = driver.find_element_by_css_selector('#rightAreaBox > div.contentsIconArea.clear > ul > li:nth-child(3) > a > span').click()

    # 登入使用者名稱
    a = driver.find_element_by_css_selector("body > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]:nth-child(1)")
    a.clear()
    a.send_keys("admin")
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
        try:
            element_object.click()
        except:
            c.append("192.168.2.6:使用者存取數量過多,請手動設定或有人正在操作")
            logout(driver)
            driver.close()
            return Ricoh2(name, driver, c)
    
    # 新增使用者
    driver.switch_to.default_content()
    iframe2 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe2)
    # 點選新增使用者
    while 1:
        try:
            driver.execute_script('javascript:AddUser()')
            break
        except:
            sleep(1)
    # 勾選使用者驗證
    while 1:
        try:
            driver.switch_to.parent_frame()
            iframe3 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
            driver.switch_to.frame(iframe3)
            elem_cert = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[2]/div/form/ul[3]/li/div/dl/dt/label").click()
            break
        except:
            # 沒有成功勾選使用者驗證
            # sleep(1)
            # driver.switch_to.default_content()
            # driver.switch_to.frame(iframe2)
            # element = driver.find_element_by_xpath('//*[@id="settingBoxButtonArea"]/ul/li[1]/a').click()
            c.append("192.168.2.6:使用者存取數量過多,請手動設定或有人正在操作")
            logout(driver)
            driver.close()
            return Ricoh2(name, driver, c)
    
    # 前往下一頁
    elem_next = driver.find_element_by_css_selector("#forwardButton > input")
    nextpage(driver, elem_next)

    # step 1 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe4 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe4)
    elem_name = driver.find_element_by_css_selector(
        "#frame_main-mdl > div > ul > li:nth-child(2) > div > dl > dd > input")
    elem_name.clear()
    elem_name.send_keys(name)
    # 前往下一頁
    elem_n = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div[2]/div/ul/li[2]/input")
    nextpage(driver, elem_n)

    # step 2 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe5 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe5)
    elem_name1 = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/form/div/div/ul/li[1]/div/dl/dd/input")
    try:
        elem_name1.send_keys(name)
    except:
        c.append("192.168.2.6:使用者存取數量過多,請手動設定或有人正在操作")
        logout(driver)
        driver.close()
        return Ricoh2(name, driver, c)

    # 下一步
    elem_n = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/div[2]/div/ul/li[2]/input")
    nextpage(driver, elem_n)

    # page 3
    
    # 送出表單
    try:
        # 新增等待三秒 避免網頁等太久
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[7]/div[3]/div/ul/li[2]/input").click()
    except:
        # 資料已存在
        logout(driver)
        c.append('192.168.231.1已存在' + name)
        return Ricoh2(name, driver, c)
    
    try:
        elem_error = driver.find_element_by_xpath('/html/body/div/div[3]/table[2]/tbody/tr/td[2]/table[2]/tbody/tr/td/form[1]/table[2]/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td').click()
        c.append("192.168.231.1:使用者存取數量過多,請手動設定或有人正在操作")
        logout(driver)
        driver.close()
        return Ricoh2(name, driver, c)
    except:
        # 登出
        logout(driver)
        c.append('成功輸入:192.168.231.1')
        return Ricoh2(name, driver, c)

def Ricoh2(name, driver, c):
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
        try:
            element_object.click()
        except:
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
            elem_cert = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[2]/div/form/ul[3]/li/div/dl/dt/label").click()
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
    elem_name1 = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/form/div/div/ul/li[1]/div/dl/dd/input")
    elem_name1.send_keys(name)
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


# 前往192.168.231.1

# printer1(name,num,driver)