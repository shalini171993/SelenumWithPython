from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.maximize_window()
driver.implicitly_wait(5)



def select_mulitple(options,value):
    for elements in options:
        for i in  range(len(value)):
            if elements.text == value[i]:
                elements.click()
                break


driver.find_element(By.ID,'justAnInputBox').click()
options = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list = ['choice 1','choice 2','choice 6 2 3','choice 4']
select_mulitple(options,value_list)
