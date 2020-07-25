from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.maximize_window()
driver.implicitly_wait(5)



def select_mulitple(options,value):
    if not value[0] == 'all':
            for elements in options:
                for i in  range(len(value)):
                    if elements.text == value[i]:
                        elements.click()
                        break
    else:
        try:
            for elements in options:
                elements.click()
        except Exception as e:
                print(e)

driver.find_element(By.ID,'justAnInputBox').click()
options = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
value_list = ['all']
select_mulitple(options,value_list)
