from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def reEvaluete(path):
  return driver.find_elements(by=By.XPATH, value=path)


driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua/ua/")
# button_catalog = driver.find_element(by=By.ID, value="fat-menu")
# button_catalog.click()
# search_input = driver.find_element(by=By.NAME, value="search")
# search_input.send_keys("Playstation") 
btn_cn = "search-form__submit"
checkboxes_xpath = """//a[@class="checkbox-filter__link"]"""
button_catalog = driver.find_element(by=By.CLASS_NAME, value=btn_cn)
search_input = driver.find_element(by=By.NAME, value="search")
search_input.send_keys("Smatphone") 
button_catalog.click()
time.sleep(1)
try: 
  time.sleep(2)
  checkboxes = driver.find_elements(by=By.XPATH, value=checkboxes_xpath)
  print(checkboxes)
  time.sleep(2)
  reEvaluete(checkboxes_xpath)[0].click()
  time.sleep(2)
  reEvaluete(checkboxes_xpath)[4].click()
  time.sleep(2)
  reEvaluete(checkboxes_xpath)[6].click()
except:
  print("Something went wrong")
time.sleep(15)
driver.quit()

