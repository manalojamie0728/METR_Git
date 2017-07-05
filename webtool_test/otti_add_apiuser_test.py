from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Login(curr):
	InputCreds = driver.find_element_by_name("username")
	InputCreds.send_keys("admin")
	InputCreds = driver.find_element_by_name("password")
	InputCreds.send_keys(curr)
	InputCreds.submit()
	time.sleep(1)

driver = webdriver.Firefox()
driver.get("http://localhost/otti_webtool")

print "[[TEST III-1: Add API User]]" # CLEAR!
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: H0jo$a7ok0

# Initialize by Logging In First
Login(pass_cycle[2])

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/add")

user = ['', 'lady_gaga']
pwd = ['', 'asdfghj', 'havey123']
test_type = ['Username Blank', 'Username Filled']
r_path = ['' , 'res01']

print("TEST 1: Check Account Existence"),
InputInfo = driver.find_element_by_name("name")
InputInfo.clear()
InputInfo.send_keys('neo')
InputInfo = driver.find_element_by_name("password")
InputInfo.clear()
InputInfo.send_keys('asdf')
InputInfo = driver.find_element_by_name("verify_password")
InputInfo.clear()
InputInfo.send_keys('asdf')
InputInfo.submit()
time.sleep(1)
print("[PASS]" if ("This Username is already taken." in driver.page_source) else "[FAIL]")

# First User - No Resource Path
for i in range(0, 2):
	for j in range(0, 3):
		for k in range(0, 3):
			print("TEST "+str(9*i+3*j+k+2)+": "+test_type[(9*i+3*j+k)/9]+", No Resource Path"),
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
				print("[PASS]" if not("Successfully created ott account." in driver.page_source) else "[FAIL]")
			else:
				print("[PASS]" if ("Successfully created ott account." in driver.page_source) else "[FAIL]")
time.sleep(1)
user_id1 = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")

print("TEST 20: Check Added User In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("lady_gaga" in driver.page_source) else "[FAIL]")

print("TEST 21: Check Added User's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/details/"+user_id1)
time.sleep(1)
print("[PASS]" if ("Details of account lady_gaga" in driver.page_source) else "[FAIL]")

print("TEST 22: Delete Added API User From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/delete/"+user_id1)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT API account." in driver.page_source) else "[FAIL]")

print("TEST 23: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("lady_gaga" in driver.page_source) else "[FAIL]")

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/add")

# Second User - With Resource Path
for i in range(0, 2):
	print("TEST "+str(24+i)+": Create with Resource Path"),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys('katy_perry')
	InputInfo = driver.find_element_by_name("password")
	InputInfo.clear()
	InputInfo.send_keys('california')
	InputInfo = driver.find_element_by_name("verify_password")
	InputInfo.clear()
	InputInfo.send_keys('california')
	if i == 0:
		driver.find_element_by_xpath("//tfoot/tr/th/button").send_keys(Keys.ENTER)
		driver.find_element_by_xpath("//input[@name='permissions[0][http_methods][]'][@value='GET']").click()
	InputInfo = driver.find_element_by_name("permissions[0][path]")
	InputInfo.clear()
	InputInfo.send_keys(r_path[i])
	InputInfo.submit()
	time.sleep(1)
	if i == 0:
		print("[PASS]" if not("Successfully created ott account." in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully created ott account." in driver.page_source) else "[FAIL]")
time.sleep(1)
user_id2 = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")

print("TEST 24: Check Added User In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("katy_perry" in driver.page_source) else "[FAIL]")

print("TEST 25: Check Added User's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/details/"+user_id2)
time.sleep(1)
print("[PASS]" if ("Details of account katy_perry" in driver.page_source) else "[FAIL]")

print("TEST 26: Delete Added API User From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/delete/"+user_id2)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT API account." in driver.page_source) else "[FAIL]")

print("TEST 27: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("katy_perry" in driver.page_source) else "[FAIL]")

time.sleep(3)
driver.quit()