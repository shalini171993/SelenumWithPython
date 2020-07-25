from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
driver.implicitly_wait(5)
driver.maximize_window()
first_name = driver.find_element(By.ID,'Form_submitForm_FirstName')
last_name = driver.find_element_by_id('Form_submitForm_LastName')
job = driver.find_element_by_name('JobTitle')
email = driver.find_element_by_id('Form_submitForm_Email')

first_name.send_keys("shalini")
last_name.send_keys("baskaran")
job.send_keys("software engineer")
email.send_keys("abc@hcl.com")
#driver.find_element_by_link_text("Features").click()



# employee_count = driver.find_element_by_id('Form_submitForm_NoOfEmployees')
# select = Select(employee_count)
# #select.select_by_index(4)
# select.select_by_visible_text('4,001 - 4,500')
#
# industry = driver.find_element_by_id('Form_submitForm_Industry')
# select = Select(industry)
# select.select_by_visible_text('Aerospace')
#
# country = driver.find_element_by_id('Form_submitForm_Country')
# select= Select(country)
# select.select_by_visible_text('India')

def select_values_from_dropDown(key,value):
    select = Select(key)
    select.select_by_visible_text(value)

industry = driver.find_element_by_id('Form_submitForm_Industry')
country = driver.find_element_by_id('Form_submitForm_Country')

select_values_from_dropDown(industry,'Aerospace')
select_values_from_dropDown(country,'India')

select = Select(industry)
list_of_options = select.options
for element in list_of_options:
    print(element.text)