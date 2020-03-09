from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from printer3 import printer3
def printer2(name, num, driver):
    c = []
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
    driver.close()
    return c
    # 20191114
