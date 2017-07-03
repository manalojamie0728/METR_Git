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

print "[[TEST V: Add/Edit User Group]]"
group_name = ['', 'abacada', 'GroupAwesome']
new_name = ['', 'abacada', 'TeamScholarly']
test_cases = ['Group Name Empty', 'Group Name Exists', 'Group Name Valid']
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: M7Ght33Mou$e

# Initialize by Logging In First
Login(pass_cycle[1])

# Part A: Add User Group
driver.get("http://localhost/otti_webtool/index.php/groups/add")
for i in range(0, 3):
	print("TEST "+str(i+1)+": "+test_cases[i]+" (Add)"),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys(group_name[i])
	for m in range(2, 9):
		Radio = driver.find_element_by_xpath("//form/div["+str(m)+"]/div/div[1]/label/input[1]")
		Radio.click()
	InputInfo.submit()
	time.sleep(1)
	if i+1 < 3:
		print("[PASS]" if not ("Successfully created user group." in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully created user group." in driver.page_source) else "[FAIL]")
time.sleep(1)
group_id = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/groups")

print("TEST 4: Check Added User Group In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("GroupAwesome" in driver.page_source) else "[FAIL]")

print("TEST 5: Check Added User Group's Details"),
driver.get("http://localhost/otti_webtool/index.php/groups/details/"+group_id)
time.sleep(1)
print("[PASS]" if ("Details of Group GroupAwesome" in driver.page_source) else "[FAIL]")

# Part B: Edit User Group
driver.get("http://localhost/otti_webtool/index.php/groups/edit/"+group_id)
for i in range(0, 3):
	print("TEST "+str(i+6)+": "+test_cases[i]+" (Edit)"),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys(new_name[i])
	for m in range(5, 8):
		Radio = driver.find_element_by_xpath("//form/div["+str(m)+"]/div/div[2]/label/input[1]")
		Radio.click()
	InputInfo.submit()
	time.sleep(1)
	if i+6 < 8:
		print("[PASS]" if not ("Successfully created user group." in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully created user group." in driver.page_source) else "[FAIL]")
time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/groups")

print("TEST 9: Check Edited User Group In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("TeamScholarly" in driver.page_source) else "[FAIL]")

print("TEST 10: Check Edited User Group's Details"),
driver.get("http://localhost/otti_webtool/index.php/groups/details/"+group_id)
time.sleep(1)
print("[PASS]" if ("Details of Group TeamScholarly" in driver.page_source) else "[FAIL]")

# Part C: Delete User Group
print("TEST 11: Delete User Group From List"),
driver.get("http://localhost/otti_webtool/index.php/groups")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/groups/delete/"+group_id)
time.sleep(1)
print("[PASS]" if ("Successfully deleted user group." in driver.page_source) else "[FAIL]")

print("TEST 12: Check Deletion Success"),
driver.get("http://localhost/otti_webtool/index.php/groups")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("TeamScholarly" in driver.page_source) else "[FAIL]")

time.sleep(2)
driver.quit()