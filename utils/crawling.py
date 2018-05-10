from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver = webdriver.Firefox(executable_path='/home/kahee/geckodriver')
driver.get('https://library.sejong.ac.kr/identity/Login.ax')

# 로그인
driver.find_element_by_name('userID').send_keys('13010063')
driver.find_element_by_name('password').send_keys('940131')
driver.find_element_by_xpath('//a[@href="javascript:identify.goLogin();"]').click()


