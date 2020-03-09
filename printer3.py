from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from time import sleep
def printer3(name, num, driver):
    c = []
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
    sleep(3)
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
    driver.close()
    return c
    # 20191114
