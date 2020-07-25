from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="C:\\Users\\shalini\\Downloads\\chromedriver\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.implicitly_wait(5)
print(driver.title)

driver.find_element(By.NAME,'q').send_keys("laptop")

list = driver.find_elements(By.CSS_SELECTOR,'ul.erkvQe li span')
print (len(list))
for element in list:
    print(element.text)
    if element.text == 'laptop table' :
        element.click()
        break

driver.quit()