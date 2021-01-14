from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.propertycapsule.com/")
driver.find_element_by_link_text("See for yourself").click()

driver.find_element_by_name("FirstName").send_keys("Umesh")
driver.find_element_by_name("LastName").send_keys("Sable")
driver.find_element_by_id("Email").send_keys("umeshsable24@gmail.com")
driver.find_element_by_id("GDPR_Opt_In__c").click()
driver.find_element_by_xpath("//div[contains(@class, 'mktoButton')]").click()
driver.find_element_by_class_name("mktoButton").click()
