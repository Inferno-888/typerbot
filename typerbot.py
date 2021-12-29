from selenium import webdriver
from waiter import wait
import keyboard
from typing import nowTyping

def type():
    URL = "https://play.typeracer.com/"
    execPath = "C:\\Users\\USER\\Downloads\\chromeDriver\\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=execPath)
    browser.get(URL)

    wait(2)  # Allow time for the page to fully load to find the start btn
    startBtn = browser.find_element_by_xpath('//*[@id="gwt-uid-1"]/a')
    startBtn.click()

    wait(5)

    i = 0
    str1 = ''
    str2 = ''
    str3 = ''

    while i < 100 and str1 == '':

        try:
            str1 = browser.find_element_by_xpath('//*[@id="gwt-uid-{}"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]'.format(i)).text
            str2 = browser.find_element_by_xpath('//*[@id="gwt-uid-{}"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]'.format(i)).text
            str3 = browser.find_element_by_xpath('//*[@id="gwt-uid-{}"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]'.format(i)).text
        except:
            pass
        i += 1

    full_text = str1 + str2 + ' ' + str3

    # Exporting to the other window...
    nowTyping(full_text)

    print(full_text)

    keyboard.wait('esc')
    keyboard.write(full_text, 0.05)
