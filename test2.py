from selenium import webdriver
from printer3 import printer3
# name = input("請輸入名稱:")   #名稱
name = '711'
num = '0'+name  #編號
driver = webdriver.Chrome() #共用的瀏覽器
printer3(name,num,driver)