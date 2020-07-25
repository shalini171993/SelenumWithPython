from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.ID,'justAnInputBox').click()


def select_mulitple(value):
    options = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')
    for elements in options:
    #print(elements.text)
        if(elements.text == value):
            elements.click()
            break

select_mulitple('choice 3')
select_mulitple('choice 6 2 3')