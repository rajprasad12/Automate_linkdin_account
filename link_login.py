######### AUTHOR : RAJ PRASAD KUIRI #########
######### email id: prasadraj954@gmail.com ########

from selenium import webdriver
driver=webdriver.Chrome(executable_path="G:\\webdriver\\chromedriver.exe")
driver.get("https://www.linkedin.com")
driver.find_element_by_name("session_key").send_keys("prasadraj954@gmail.com")
driver.find_element_by_name("session_password").send_keys("bipula@123")
driver.find_element_by_class_name("sign-in-form__submit-btn").click()
driver.find_element_by_class_name("nav-item__title nav-item__dropdown-trigger--title").click()
'''create your xpath (tagename[@attribute='value']'''
driver.find_element_by_xpath("//Sign out[@data-control-name='nav.settings_signout']")
print("all good")
