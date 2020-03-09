#from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
#name = input("請輸入名稱:")   #名稱
#num = '0'+name  #編號
#driver = webdriver.Chrome() #共用的瀏覽器
def printer1 (name,num,driver):
    driver.get('http://192.168.2.2/')
    #2020/3/9新增(進入被阻擋的連線)
    advanced = driver.find_element_by_css_selector('#details-button')
    advanced.click()
    proceed = driver.find_element_by_css_selector('#proceed-link')
    proceed.click()
    #-----------
    frame = driver.find_element_by_xpath('/html/frameset/frame')
    driver.switch_to.frame(frame)
    # driver.implicitly_wait(20)
    elem_1 = driver.find_element_by_css_selector('#documentColor')

    elem_1.click()

    elem_2 = driver.find_element_by_xpath('/html/body/form/div/div[3]/div[2]/div[1]/div/div/div[17]/table/tbody/tr/td[2]/div/div[2]/u/a/span')
    elem_2.click()
    for i in range(0,5):
        sleep(1)
        print('我睡著了')
    print('我醒了喔!!!')
    frame2 = driver.find_element_by_xpath('//*[@id="printingjobs"]')
    driver.switch_to.frame(frame2)


    elem_3 = driver.find_element_by_css_selector('#contentrowtable > tbody > tr:nth-child(1) > td:nth-child(6)')
    elem_3.click()
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

    try:
        elem_submit = driver.find_element_by_name('submit001')

        sleep(3)
        elem_submit.click()
        printer2(name, num, driver)
    except UnexpectedAlertPresentException:
        print("192.168.2.2已存在", name)
        printer2(name,num,driver)
def printer2(name,num,driver):
    driver.get('http://192.168.2.190/')
    frame = driver.find_element_by_xpath('/html/frameset/frame')
    driver.switch_to.frame(frame)
    # driver.implicitly_wait(20)
    elem_1 = driver.find_element_by_xpath('//*[@id="tm3"]/div[1]')

    elem_1.click()

    elem_2 = driver.find_element_by_xpath('//*[@id="s6"]')
    elem_2.click()
    frame2 = driver.find_element_by_xpath('//*[@id="printingjobs"]')
    driver.switch_to.frame(frame2)
    elem_3 = driver.find_element_by_css_selector('#contentrowtable > tbody > tr:nth-child(1) > td:nth-child(6)')
    elem_3.click()
    driver.switch_to.parent_frame()

    frame3 = driver.find_element_by_id("alphardmaedasboxadd")
    driver.switch_to.frame(frame3)
    elem_4 = driver.find_element_by_css_selector(
        '#outerdiv > table:nth-child(2) > tbody > tr:nth-child(3) > td.style194 > input')
    elem_4.clear()
    elem_4.send_keys(num)
    elem_5 = driver.find_element_by_css_selector('#w300px')
    elem_5.clear()
    elem_5.send_keys(name)
    elem_open = driver.find_element_by_css_selector(
        '#outerdiv > table:nth-child(2) > tbody > tr:nth-child(15) > td.style194 > label:nth-child(1) > input[type=radio]')
    elem_open.click()
    driver.implicitly_wait(20)

    elem_del = driver.find_element_by_css_selector(
        '#outerdiv > table:nth-child(2) > tbody > tr:nth-child(20) > td.style194 > label:nth-child(1) > input[type=radio]')
    # elem_del.location_once_scrolled_into_view
    elem_del.click()
    elem_days = driver.find_element_by_css_selector(
        '#outerdiv > table:nth-child(2) > tbody > tr:nth-child(16) > td.style194 > input')
    elem_days.clear()
    elem_days.send_keys('1')

    # elem_submit = driver.find_element_by_xpath('//*[@id="submit"]')

    try:
        elem_submit = driver.find_element_by_name('submit001')

        sleep(3)
        elem_submit.click()
        printer3(name,num,driver)
    except UnexpectedAlertPresentException:
        print("192.168.2.190已存在", name)
        printer3(name, num, driver)
def printer3(name,num,driver):
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
    frame2 = driver.find_element_by_xpath('//*[@id="printingjobs"]')
    driver.switch_to.frame(frame2)
    sleep(5)
    elem_3 = driver.find_element_by_xpath('/html/body/form/div/div/div[1]/div[1]/div[1]')
    elem_3.click()
    driver.switch_to.parent_frame()

    frame3 = driver.find_element_by_id("alphardmaedasabadd")
    driver.switch_to.frame(frame3)
    elem_4 = driver.find_element_by_css_selector(
        '#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(1) > td.style194 > input')
    elem_4.clear()
    elem_4.send_keys(num)
    elem_5 = driver.find_element_by_css_selector('#w300px')
    elem_5.clear()
    elem_5.send_keys(name)
    elem_open = driver.find_element_by_css_selector(
        '#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(13) > td.style194 > div')
    elem_open.click()
    driver.implicitly_wait(20)

    elem_del = driver.find_element_by_css_selector(
        '#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(18) > td.style194 > div')
    elem_del.location_once_scrolled_into_view
    elem_del.click()
    elem_days = driver.find_element_by_css_selector(
        '#dataFixed > div:nth-child(1) > table > tbody > tr:nth-child(14) > td.style194 > input')
    elem_days.clear()
    elem_days.send_keys('1')

    try:
        elem_submit = driver.find_element_by_css_selector(
            '#footerFixed > div > div.wrap.right > input[type=submit]:nth-child(1)')
        elem_submit.click()
        Ricoh(name,driver)
    except UnexpectedAlertPresentException:
        print("192.168.231.2已存在", name)
        Ricoh(name, driver)
def Ricoh(name,driver):
    driver.get('http://192.168.231.1/web/guest/tw/websys/webArch/mainFrame.cgi')

    # 登入
    iframe = driver.find_element_by_css_selector('html > frameset > frame:nth-child(1)')
    driver.switch_to.frame(iframe)
    elem_enter = driver.find_element_by_css_selector(
        '#rightAreaBox > div.contentsIconArea.clear > ul > li:nth-child(3) > a > span').click()

    # 登入使用者名稱
    a = driver.find_element_by_css_selector(
        "body > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]:nth-child(1)")
    a.clear()
    a.send_keys("admin")
    # 登入
    elem_login = driver.find_element_by_css_selector(
        "body > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(6) > td:nth-child(2) > input[type=submit]").click()

    # 裝置管理,通訊錄
    iframe1 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe1)
    elem_manage = driver.find_element_by_css_selector(
        "#sectionLinks > ul > li:nth-child(2) > div > a > span.menuText").click()
    elem_address = driver.find_element_by_css_selector(
        "#sectionLinks > ul > li:nth-child(2) > ul > li:nth-child(2) > a").click()

    # 新增使用者
    driver.switch_to.parent_frame()
    """
    for i in range(0, 5):
        sleep(1)
        print('sleep!!')
    print('Now I am winner!!')
    """
    iframe2 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe2)
    elem_add = driver.find_element_by_xpath('//*[@id="settingBoxButtonArea"]/ul/li[1]/a')
    def tryclick(driver, xpath, count=0):
        try:
            elem_add = driver.find_element_by_xpath('//*[@id="settingBoxButtonArea"]/ul/li[1]/a')
            elem_add.click()
        except:
            sleep(2)
            count+=1
            if(count<2):
                tryclick(driver, xpath, count)
            else:
                print('192.168.231.1:使用者存取數量過多,請手動輸入')
                Ricoh2(name, driver)
    tryclick(driver, '//*[@id="settingBoxButtonArea"]/ul/li[1]/a')
    sleep(3)
    # 勾選使用者驗證
    driver.switch_to.parent_frame()
    iframe3 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe3)
    driver.implicitly_wait(20)
    elem_cert = driver.find_element_by_xpath(
        "/html/body/div/div[3]/div/div[2]/div[2]/div/form/ul[3]/li/div/dl/dt/label").click()
    # 前往下一頁
    elem_next = driver.find_element_by_css_selector("#forwardButton > input").click()

    # step 1 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe4 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe4)
    elem_name = driver.find_element_by_css_selector(
        "#frame_main-mdl > div > ul > li:nth-child(2) > div > dl > dd > input")
    elem_name.clear()
    elem_name.send_keys(name)
    # 前往下一頁
    elem_n = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div[2]/div/ul/li[2]/input").click()
    sleep(2)

    # step 2 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe5 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe5)
    elem_name1 = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/form/div/div/ul/li[1]/div/dl/dd/input")
    elem_name1.send_keys(name)
    # 下一步
    driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/div[2]/div/ul/li[2]/input").click()
    sleep(2)
    # 此使用者名稱已存在
    # = BeautifulSoup(driver.page_source, "html.parser")
    # ids = soup.find('input', id = "USERNAME_E")
    # print(ids.get("value"))

    # with open('test.html', mode='w', encoding='utf-8') as file:
    #  file.write(str(soup))

    # driver.close()

    # page 3
    try:
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[7]/div[3]/div/ul/li[2]/input").click()
        Ricoh2(name,driver)
    except:
        print('192.168.231.1:此使用者名稱已存在')
        Ricoh2(name, driver)

def Ricoh2(name, driver):
    # 前往192.168.2.6
    driver.get('http://192.168.2.6/web/guest/tw/websys/webArch/mainFrame.cgi')
    sleep(2)
    # 登入
    iframe = driver.find_element_by_css_selector('html > frameset > frame:nth-child(1)')
    driver.switch_to.frame(iframe)
    elem_enter = driver.find_element_by_css_selector('#rightAreaBox > div.contentsIconArea.clear > ul > li:nth-child(3) > a > span').click()

    # 登入使用者名稱
    a = driver.find_element_by_css_selector(
    "body > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > input[type=text]:nth-child(1)")
    a.clear()
    a.send_keys("admin")
    # 登入
    elem_login = driver.find_element_by_css_selector("body > table > tbody > tr:nth-child(6) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(6) > td:nth-child(2) > input[type=submit]").click()

    # 裝置管理,通訊錄
    iframe1 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe1)
    elem_manage = driver.find_element_by_css_selector("#sectionLinks > ul > li:nth-child(2) > div > a > span.menuText").click()
    elem_address = driver.find_element_by_css_selector("#sectionLinks > ul > li:nth-child(2) > ul > li:nth-child(2) > a").click()

    # 新增使用者
    driver.switch_to.default_content()
    iframe2 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe2)
    try:
        elem_add = driver.find_element_by_xpath('//*[@id="settingBoxButtonArea"]/ul/li[1]/a').click()
    except:
        print("192.168.2.6:使用者存取數量過多,請手動設定")
        driver.close()

    # 勾選使用者驗證
    driver.switch_to.parent_frame()
    iframe3 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe3)
    driver.implicitly_wait(20)
    elem_cert = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[2]/div/form/ul[3]/li/div/dl/dt/label").click()
    # 前往下一頁
    elem_next = driver.find_element_by_css_selector("#forwardButton > input").click()

    # step 1 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe4 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe4)
    elem_name = driver.find_element_by_css_selector("#frame_main-mdl > div > ul > li:nth-child(2) > div > dl > dd > input")
    elem_name.clear()
    elem_name.send_keys(name)
    # 前往下一頁
    elem_n = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[3]/div[2]/div/ul/li[2]/input").click()
    sleep(5)

    # step 2 , 輸入名稱
    driver.switch_to.parent_frame()
    iframe5 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(2)")
    driver.switch_to.frame(iframe5)
    elem_name1 = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/form/div/div/ul/li[1]/div/dl/dd/input")
    elem_name1.send_keys(name)
    # 下一步
    driver.find_element_by_xpath("/html/body/div/div[3]/div/div[6]/div[2]/div/ul/li[2]/input").click()


    try:
        driver.find_element_by_xpath("/html/body/div/div[3]/div/div[7]/div[3]/div/ul/li[2]/input").click()
        driver.close()
    except:
        driver.switch_to.parent_frame()
        iframe6 = driver.find_element_by_css_selector("html > frameset > frame:nth-child(1)")
        driver.switch_to.frame(iframe6)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/ul/li[4]/a").click()
        driver.close()
        print('192.168.2.6:此使用者名稱已存在')

    print("程式已結束")

# 前往192.168.231.1

#printer1(name,num,driver)