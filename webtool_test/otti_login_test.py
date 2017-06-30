from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("http://localhost/otti_webtool")

print "[[TEST I: Log-In Page]]"
user = ['', 'adm1n', 'admin']
pwd = ['', 'password', 'admin']
test_cases = ['Blank User/Blank Password', 'Blank User/Wrong Password', 'Blank User/Right Password',
				'Wrong User/Blank Password', 'Wrong User/Wrong Password', 'Wrong User/Right Password',
				'Right User/Blank Password', 'Right User/Wrong Password', 'Right User/Right Password']

for i in range(0, 3):
	for j in range(0, 3):
		print("TEST "+str(3*i+j+1)+": "+test_cases[3*i+j]),
		inputCreds = driver.find_element_by_name("username")
		inputCreds.send_keys(user[i])
		inputCreds = driver.find_element_by_name("password")
		inputCreds.send_keys(pwd[j])
		inputCreds.submit()
		time.sleep(1)
		if (3*i+j+1) < 9:
			print("[PASS]" if ("Incorrect" in driver.page_source) else "[FAIL]")
		else:
			print("[PASS]" if ("Welcome!" in driver.page_source) else "[FAIL]")

time.sleep(2)
driver.quit()