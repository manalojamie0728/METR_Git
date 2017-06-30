from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://www.google.com")
print driver.title

inputElement = driver.find_element(By.NAME, "q")
inputElement.send_keys("cheese!")
inputElement.submit()

try:
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    print driver.title
finally:
    driver.quit()
