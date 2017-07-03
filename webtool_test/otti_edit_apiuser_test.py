from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("http://localhost/otti_webtool")

print "[[TEST III-2: Edit API User]]"
# Initialize by Logging In First
InputCreds = driver.find_element_by_name("username")
InputCreds.send_keys("admin")
InputCreds = driver.find_element_by_name("password")
InputCreds.send_keys("admin")
InputCreds.submit()

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/add")
InputInfo = driver.find_element_by_name("name")
InputInfo.clear()
InputInfo.send_keys('katy_perry')
InputInfo = driver.find_element_by_name("password")
InputInfo.clear()
InputInfo.send_keys('california')
InputInfo = driver.find_element_by_name("verify_password")
InputInfo.clear()
InputInfo.send_keys('california')
InputInfo.submit()
time.sleep(1)
user_id1 = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/edit_account_details/"+user_id1)

user = ['', 'pitbull']
pwd = ['', 'asdfghj', 'havey123']
test_type = ['Username Blank', 'Username Filled']
r_path = ['' , 'res02']
meth = ['GET', 'POST', 'PUT', 'DELETE']

for i in range(0, 2):
	for j in range(0, 3):
		for k in range(0, 3):
			print("TEST "+str(9*i+3*j+k+1)+": Edit Account Details, "+test_type[(9*i+3*j+k)/9]),
			InputInfo = driver.find_element_by_name("name")
			InputInfo.clear()
			InputInfo.send_keys(user[i])
			InputInfo = driver.find_element_by_name("password")
			InputInfo.clear()
			InputInfo.send_keys(pwd[k])
			InputInfo = driver.find_element_by_name("verify_password")
			InputInfo.clear()
			InputInfo.send_keys(pwd[j])
			InputInfo.submit()
			time.sleep(1)
			if (9*i+3*j+k+1) < 18:
				print("[PASS]" if not("Successfully updated account password." in driver.page_source) else "[FAIL]")
			else:
				print("[PASS]" if ("Successfully updated account password." in driver.page_source) else "[FAIL]")
time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")

print("TEST 19: Check Edited User In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("pitbull" in driver.page_source) else "[FAIL]")

print("TEST 20: Check Edited User's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/details/"+user_id1)
time.sleep(1)
print("[PASS]" if ("Details of account pitbull" in driver.page_source) else "[FAIL]")

driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/edit_permissions/"+user_id1)
driver.find_element_by_xpath("//tfoot/tr/th/button").send_keys(Keys.ENTER)
InputInfo = driver.find_element_by_name("permissions[0][path]")
InputInfo.clear()
InputInfo.send_keys(r_path[1])

for i in range(0, 4):
	print("TEST "+str(21+i)+": Edit Permission "+meth[i]),
	driver.find_element_by_xpath("//input[@name='permissions[0][http_methods][]'][@value='"+meth[i]+"']").click()
	driver.find_element_by_xpath("//button[@type='submit']").send_keys(Keys.ENTER)
	time.sleep(1)
	print("[PASS]" if (meth[i] in driver.page_source) else "[FAIL]")
	driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/edit_permissions/"+user_id1)

print("TEST 25: Remove Permissions From User"),
driver.find_element_by_xpath("//tbody/tr/td/button").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//button[@type='submit']").send_keys(Keys.ENTER)
time.sleep(1)
print("[PASS]" if not('GET' in driver.page_source) else "[FAIL]")

print("TEST 26: Delete Edited API User From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/delete/"+user_id1)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT API account." in driver.page_source) else "[FAIL]")

print("TEST 27: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("pitbull" in driver.page_source) else "[FAIL]")

time.sleep(3)
driver.quit()