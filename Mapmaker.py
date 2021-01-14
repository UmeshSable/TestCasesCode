from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.propertycapsule.com/")
driver.find_element_by_link_text("Map Maker").click()

