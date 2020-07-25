from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


browserName = "opera"

if browserName == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("driver not defined")
    raise Exception("driver is not mentioned")
driver.get("https://app.hubspot.com/login")
driver.implicitly_wait(7)
driver.find_element(By.XPATH,"//input[@id ='username']").send_keys("shalinibaskaran17@gmail.com")
driver.find_element(By.ID,"password").send_keys("shalini")
driver.find_element(By.XPATH,"//span[@class='private-checkbox__indicator']").click()
driver.find_element_by_id('loginBtn').click()
print(driver.title)