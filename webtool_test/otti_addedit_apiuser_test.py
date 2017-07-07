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

print "[[TEST III: Add/Edit API User]]" # CLEAR! ***
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: H0jo$a7ok0

# Initialize by Logging In First
Login(pass_cycle[2])

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/add")

user = ['', 'lady_gaga', 'katy_perry', 'pitbull']
pwd = ['', 'asdfghj', 'havey123', 'california', 'mistahworldwide']
test_type = ['No Resource Path', 'With Resource Path']
r_path = ['' , 'res01', 'res02']
meth = ['GET', 'POST', 'PUT', 'DELETE']
test_cases = ['Missing Username', 'Missing Password', 'Missing Verify Password',
			'Incorrect Verify Password', 'Complete Details']

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

# Part A: Add User 1 - No Resource Path
for i in range(0, 5):
	print ("TEST "+str(i+2)+": "+test_cases[i]+"("+test_type[0]+")"),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys(user[1])
	InputInfo = driver.find_element_by_name("password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[2])
	InputInfo = driver.find_element_by_name("verify_password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[2])
	if i == 0:
		driver.find_element_by_name("name").clear()
	elif i == 1:
		driver.find_element_by_name("password").clear()
	elif i == 2:
		driver.find_element_by_name("verify_password").clear()
	elif i == 3:
		driver.find_element_by_name("verify_password").clear()
		driver.find_element_by_name("verify_password").send_keys(pwd[1])
	InputInfo.submit()
	time.sleep(1)
	if (i+2) < 6:
		print("[PASS]" if not("Successfully created ott account." in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully created ott account." in driver.page_source) else "[FAIL]")

time.sleep(1)
user_id1 = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")

print("TEST 7: Check Added User In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("lady_gaga" in driver.page_source) else "[FAIL]")

print("TEST 8: Check Added User's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/details/"+user_id1)
time.sleep(1)
print("[PASS]" if ("Details of account lady_gaga" in driver.page_source) else "[FAIL]")

# Part B: Delete User 1
print("TEST 9: Delete Added API User From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/delete/"+user_id1)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT API account." in driver.page_source) else "[FAIL]")

print("TEST 10: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("lady_gaga" in driver.page_source) else "[FAIL]")

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/add")

# Part C: Second User - With Resource Path
test_cases.insert(4, 'Missing Resource Path')
for i in range(0, 6):
	print ("TEST "+str(i+11)+": "+test_cases[i]+"("+test_type[1]+")"),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys(user[2])
	InputInfo = driver.find_element_by_name("password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[3])
	InputInfo = driver.find_element_by_name("verify_password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[3])
	if i == 0:
		driver.find_element_by_name("name").clear()
	elif i == 1:
		driver.find_element_by_name("password").clear()
	elif i == 2:
		driver.find_element_by_name("verify_password").clear()
	elif i == 3:
		driver.find_element_by_name("verify_password").clear()
		driver.find_element_by_name("verify_password").send_keys(pwd[2])
	if i > 3:
		if i == 4:
			driver.find_element_by_xpath("//tfoot/tr/th/button").send_keys(Keys.ENTER)
			driver.find_element_by_xpath("//input[@name='permissions[0][http_methods][]'][@value='POST']").click()
		InputInfo = driver.find_element_by_name("permissions[0][path]")
		InputInfo.clear()
		InputInfo.send_keys(r_path[i-4])
	InputInfo.submit()
	time.sleep(1)
	if (i+11) < 16:
		print("[PASS]" if not("Successfully created ott account." in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully created ott account." in driver.page_source) else "[FAIL]")

time.sleep(1)
user_id2 = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")

print("TEST 17: Check Added User In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("katy_perry" in driver.page_source) else "[FAIL]")

print("TEST 18: Check Added User's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/details/"+user_id2)
time.sleep(1)
print("[PASS]" if ("Details of account katy_perry" in driver.page_source) else "[FAIL]")

# Part D: Edit API User Details
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/edit_account_details/"+user_id2)
test_cases.pop(4)
for i in range(0, 5):
	print("TEST "+str(i+19)+": "+test_cases[i]+" (Edit Account)"),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys(user[3])
	InputInfo = driver.find_element_by_name("password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[4])
	InputInfo = driver.find_element_by_name("verify_password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[4])
	if i == 0:
		driver.find_element_by_name("name").clear()
	elif i == 1:
		driver.find_element_by_name("password").clear()
	elif i == 2:
		driver.find_element_by_name("verify_password").clear()
	elif i == 3:
		driver.find_element_by_name("verify_password").clear()
		driver.find_element_by_name("verify_password").send_keys(pwd[3])
	InputInfo.submit()
	time.sleep(1)
	if (i+19) < 23:
		print("[PASS]" if not("Successfully updated account password." in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully updated account password." in driver.page_source) else "[FAIL]")
time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")

print("TEST 24: Check Edited User In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("pitbull" in driver.page_source) else "[FAIL]")

print("TEST 25: Check Edited User's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/details/"+user_id2)
time.sleep(1)
print("[PASS]" if ("Details of account pitbull" in driver.page_source) else "[FAIL]")

driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/edit_permissions/"+user_id2)
InputInfo = driver.find_element_by_name("permissions[0][path]")
InputInfo.clear()
InputInfo.send_keys(r_path[2])

# Part E: Edit API User Permissions
for i in range(0, 4):
	print("TEST "+str(i+26)+": Edit Permission "+meth[i]),
	driver.find_element_by_xpath("//input[@name='permissions[0][http_methods][]'][@value='"+meth[i]+"']").click()
	driver.find_element_by_xpath("//button[@type='submit']").send_keys(Keys.ENTER)
	time.sleep(1)
	if (i+26) == 27:
		print("[PASS]" if not (meth[i] in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if (meth[i] in driver.page_source) else "[FAIL]")
	driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/edit_permissions/"+user_id2)

print("TEST 30: Remove Permissions From User"),
driver.find_element_by_xpath("//tbody/tr/td/button").send_keys(Keys.ENTER)
driver.find_element_by_xpath("//button[@type='submit']").send_keys(Keys.ENTER)
time.sleep(1)
print("[PASS]" if not('GET' in driver.page_source) else "[FAIL]")

# Part F: Delete API User
print("TEST 31: Delete Added API User From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_api_accounts/delete/"+user_id2)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT API account." in driver.page_source) else "[FAIL]")

print("TEST 32: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("pitbull" in driver.page_source) else "[FAIL]")

time.sleep(2)
driver.quit()