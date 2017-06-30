from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
print driver.title

FN = "Kara"
SN = "Levine"
email = "levinekara@yahoo.com"
password = "QWERTYuiop1234567890"

inputElem = driver.find_element(By.NAME, "firstname")
inputElem.send_keys(FN)
inputElem = driver.find_element(By.NAME, "lastname")
inputElem.send_keys(SN)
inputElem = driver.find_element(By.NAME, "reg_email__")
inputElem.send_keys(email)
inputElem = driver.find_element(By.NAME, "reg_email_confirmation__")
inputElem.send_keys(email)
inputElem = driver.find_element(By.NAME, "reg_passwd__")
inputElem.send_keys(password)
time.sleep(1)

dropElem = driver.find_element(By.ID, "month")
dropElem.send_keys("Apr")
dropElem = driver.find_element(By.ID, "day")
dropElem.send_keys("15")
dropElem = driver.find_element(By.ID, "year")
dropElem.send_keys("1995")
time.sleep(1)

radio = driver.find_element(By.ID, "u_0_i")
radio.click()

subButton = driver.find_element(By.NAME, "websubmit")
subButton.click()

time.sleep(5)
print driver.title
driver.find_element_by_xpath("//*[contains(text(), 'Log Out')]").click()

time.sleep(5)
print "LOGIN SUCCESSFUL"
driver.quit()
