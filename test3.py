from selenium import webdriver
option=webdriver.ChromeOptions()
option.add_argument('headless')

from printer1 import printer1
name = input("請輸入名稱:")   #名稱
num = '0'+name  #編號
driver = webdriver.Chrome(chrome_options=option) #共用的瀏覽器
printer1(name,num,driver)