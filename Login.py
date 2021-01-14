from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://maps.propertycapsule.com/map/sign-up")
driver.find_element_by_name("email").send_keys("umeshsable24@gmail.com")
driver.find_element_by_name("password").send_keys("Munnabhai@24")
driver.find_element_by_xpath("//div[contains(@class, 'btn login-signup-btn')]").click()
driver.find_element_by_class_name("btn login-signup-btn").click()