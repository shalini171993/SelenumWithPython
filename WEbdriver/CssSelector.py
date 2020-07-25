from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get("https://app.hubspot.com/login")
#driver.implicitly_wait(5)
#driver.find_element(By.CSS_SELECTOR,'input.form-control.private-form__control.login-email').send_keys("abc")
#driver.find_element_by_link_text('Sign up').click()

#list = driver.find_elements(By.TAG_NAME,'a')
#print(len(list))

driver.get('https://www.amazon.in/')
list = driver.find_elements(By.TAG_NAME,'a')
print(len(list))
#for element in list:
    #print(element.text)
    #print(element.get_attribute('href'))

img_list = driver.find_elements_by_tag_name('img')
print(len(img_list))
for element in img_list:
    print(element.get_attribute('src'))
driver.quit()



#class="form-control private-form__control login-email"