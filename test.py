from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

import os
import time
from visual_test import checkpoint

try:
    fol_name='baseline'
    os.makedirs(fol_name)
except:
    fol_name='test_imgs'
    os.makedirs(fol_name,exist_ok=True)

#browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.maximize_window()
browser.set_page_load_timeout(20)
browser.get('http://blazedemo.com/index.php')

#css injection
browser.execute_script("document.getElementsByClassName('form-inline')[1].setAttribute('style','color:#fff;border:#fff');")
#browser.execute_script("document.getElementsByClassName('form-inline')[1].setAttribute('style','color: #fff;border: #fff';);")
time.sleep(3)

browser.save_screenshot(os.path.join(fol_name,(browser.title)+'.png'))
print(checkpoint((browser.title)))


frm_city = Select(browser.find_element_by_name('fromPort'))
frm_city.select_by_visible_text('Paris')

to_city = Select(browser.find_element_by_name('toPort'))
to_city.select_by_visible_text('New York')

browser.find_element_by_xpath("//input[@value='Find Flights']").click()
time.sleep(2)

browser.save_screenshot(os.path.join(fol_name,(browser.title)+'.png'))
print(checkpoint(browser.title))

browser.find_element_by_xpath("(//input[@value='Choose This Flight'])[1]").click()

browser.save_screenshot(os.path.join(fol_name,(browser.title)+'.png'))
print(checkpoint(browser.title))

browser.find_element_by_id('inputName').send_keys('bits n bytes')
browser.find_element_by_id('address').send_keys('bits n bytes')
browser.find_element_by_id('city').send_keys('bits n bytes')
browser.find_element_by_id('state').send_keys('bits n bytes')
browser.find_element_by_id('zipCode').send_keys('bits n bytes')
browser.find_element_by_id('creditCardNumber').send_keys('bits n bytes')
browser.find_element_by_id('creditCardMonth').send_keys('bits n bytes')
browser.find_element_by_id('creditCardYear').send_keys('bits n bytes')
browser.find_element_by_id('nameOnCard').send_keys('bits n bytes')
browser.find_element_by_id('nameOnCard').send_keys('bits n bytes')
browser.find_element_by_xpath("//input[@value='Purchase Flight']").click()

time.sleep(3)
browser.quit()