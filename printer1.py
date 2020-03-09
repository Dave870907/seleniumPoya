from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from printer2 import printer2
from selenium.webdriver.support.wait import WebDriverWait
def a(driver, b):
    return driver.find_element_by_xpath(b)

def printer1 (name, num, driver):

    driver.get('https://192.168.2.2/')
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
        driver.close()
        return c
       
    # print("192.168.2.2已存在", name)
    c.append("192.168.2.2已存在" + name)
    driver.close()
    return c
   
    

