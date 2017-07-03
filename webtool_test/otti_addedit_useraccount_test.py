from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Login(uname, curr):
	InputCreds = driver.find_element_by_name("username")
	InputCreds.send_keys(uname)
	InputCreds = driver.find_element_by_name("password")
	InputCreds.send_keys(curr)
	InputCreds.submit()
	time.sleep(1)

### URL Links ###
# http://localhost/otti_webtool/index.php/users
# http://localhost/otti_webtool/index.php/users/add
# http://localhost/otti_webtool/index.php/users/edit/4
# http://localhost/otti_webtool/index.php/users/reset_password/4
# http://localhost/otti_webtool/index.php/users/block/4
# http://localhost/otti_webtool/index.php/users/unblock/4
# http://localhost/otti_webtool/index.php/groups/delete/4
# http://localhost/otti_webtool/index.php/logout
### URL Links ###

### Page Responses ###
# Successfully created user account.
# Successfully updated user account.
# Successfully changed password.
# Successfully reset password.
# Successfully blocked user.
# Successfully unblocked user.
# User account expired.
# User is blocked.
# Change UA03's Password
# Cannot delete group.
### Page Responses ###

driver = webdriver.Firefox()
driver.get("http://localhost/otti_webtool")

print "[[TEST VI: User Account Operations]]"
group = ['', 'GroupAdd', 'GroupEdit']
username = ['', 'UA01', 'UA02', 'UA03']
pwd = ['', 'saranghae', 'LifeSt3@ler', 'W@rl0rdZ']
new_pwd = ['', 'kudosaranghae', 'Caf3L@te']
email = ['', 'UA01@metr.com.ph', 'UA02@metr.com.ph', 'UA03@metr.com.ph']
new_email = ['', 'UA03_new@metr.com.ph']
user_expiry = ['', '2016-07-01', '2018-07-01']
user_id = []
test_cases01 = ['Add - Missing Group', 'Add - Missing Username', 'Add - Password Test (Blank/Blank)',
			'Add - Password Test (Blank/Invalid)', 'Add - Password Test (Blank/Valid)', 'Add - Password Test (Invalid/Blank)',
			'Add - Password Test (Invalid/Invalid)', 'Add - Password Test (Invalid/Valid)', 'Add - Password Test (Valid/Blank)', 
			'Add - Password Test (Valid/Invalid)', 'Add - Password Test (Valid/Valid)', 'Add - Missing Email']
test_cases02 = ['Add - UA01 (Expired)', 'Add - UA02 (Blocked)', 'Add - UA03 (Valid, Change Password)']
test_cases03 = ['Edit - Password Test (Blank/Blank)', 'Edit - Password Test (Blank/Invalid)', 'Edit - Password Test (Blank/Valid)',
			'Edit - Password Test (Invalid/Blank)', 'Edit - Password Test (Invalid/Invalid)', 'Edit - Password Test (Invalid/Valid)',
			'Edit - Password Test (Valid/Blank)', 'Edit - Password Test (Valid/Invalid)', 'Edit - Password Test (Valid/Valid)']
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: M7Ght33Mou$e

# Initialize by Logging In First
Login("admin", pass_cycle[1])

# Part A: Add User Account(s) - Fail
driver.get("http://localhost/otti_webtool/index.php/users/add")
for i in range(0, 12):
	print("TEST "+str(i+1)+": "+test_cases01[i]),
	InputInfo = driver.find_element_by_xpath("//select[@name='group_id']/option[3]")
	InputInfo.click()
	InputInfo = driver.find_element_by_name("username")
	InputInfo.clear()
	InputInfo.send_keys(username[1])
	InputInfo = driver.find_element_by_name("fullname")
	InputInfo.clear()
	InputInfo.send_keys("METR User01")
	InputInfo = driver.find_element_by_name("email")
	InputInfo.clear()
	InputInfo.send_keys(email[1])
	InputInfo = driver.find_element_by_name("user_expiry")
	InputInfo.send_keys(user_expiry[2])
	if i == 0:
		driver.find_element_by_xpath("//select[@name='group_id']/option[1]").click()
	elif i == 1:
		driver.find_element_by_name("username").clear()
	elif ((i > 1) and (i < 11)):
		InputInfo = driver.find_element_by_name("password")
		InputInfo.clear()
		InputInfo.send_keys(pwd[(i-2)/3])
		InputInfo = driver.find_element_by_name("confirm_password")
		InputInfo.clear()
		InputInfo.send_keys(pwd[(i-2)%3])
	elif i == 11:
		driver.find_element_by_name("email").clear()
	InputInfo.submit()
	time.sleep(1)
	print("[PASS]" if not ("Successfully created user account." in driver.page_source) else "[FAIL]")

# Part B: Add User Account(s) - Success
for i in range(0, 3):
	driver.get("http://localhost/otti_webtool/index.php/users/add")
	print("TEST "+str(i+13)+": "+test_cases02[i]),
	InputInfo = driver.find_element_by_xpath("//select[@name='group_id']/option[3]")
	InputInfo.click()
	InputInfo = driver.find_element_by_name("username")
	InputInfo.clear()
	InputInfo.send_keys(username[i+1])
	InputInfo = driver.find_element_by_name("password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[2])
	InputInfo = driver.find_element_by_name("confirm_password")
	InputInfo.clear()
	InputInfo.send_keys(pwd[2])
	InputInfo = driver.find_element_by_name("fullname")
	InputInfo.clear()
	InputInfo.send_keys(username[i+1])
	InputInfo = driver.find_element_by_name("email")
	InputInfo.clear()
	InputInfo.send_keys(email[i+1])
	InputInfo = driver.find_element_by_name("user_expiry")
	InputInfo.send_keys(user_expiry[2])
	Radio = driver.find_element_by_xpath('//form/div[8]/div/div[2]/label/input')
	Radio.click()
	Radio = driver.find_element_by_xpath('//form/div[9]/div/div[2]/label/input')
	Radio.click()
	if i == 0:
		driver.find_element_by_name("user_expiry").send_keys(user_expiry[1])
	elif i == 1:
		driver.find_element_by_xpath('//form/div[8]/div/div[1]/label/input')
	elif i == 2:
		driver.find_element_by_xpath('//form/div[9]/div/div[1]/label/input')
	InputInfo.submit()
	time.sleep(1)
	print("[PASS]" if ("Successfully created user account." in driver.page_source) else "[FAIL]")
	time.sleep(1)
	user_id.append(driver.current_url.split('/')[-1])

for i in range(0, 3):
	print("TEST "+str(i+16)+": Check Added User Account in List ("+username[i+1]+")"),
	driver.get("http://localhost/otti_webtool/index.php/users")
	time.sleep(1)
	driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
	time.sleep(1)
	print("[PASS]" if (user_id[i] in driver.page_source) else "[FAIL]")

print("TEST 19: Check Added User's (UA03) Details"),
driver.get("http://localhost/otti_webtool/index.php/groups/details/"+user_id[2])
time.sleep(1)
print("[PASS]" if ("Username UA03" in driver.page_source) else "[FAIL]")

print("TEST 20: Attempt User Group (GroupAdd) Deletion"),
driver.get("http://localhost/otti_webtool/index.php/groups/delete/4")
time.sleep(1)
print("[PASS]" if ("Cannot delete group." in driver.page_source) else "[FAIL]")

# Part C: Login to User Accounts
driver.get("http://localhost/otti_webtool/index.php/logout")
for i in range(0, 3):
	if i == 0: #UA01
		print("TEST 21: UA01 - Account Expired Login"),
		inputCreds = driver.find_element_by_name("username")
		inputCreds.send_keys(username[i+1])
		inputCreds = driver.find_element_by_name("password")
		inputCreds.send_keys(pwd[2])
		inputCreds.submit()
		time.sleep(1)
		print("[PASS]" if ("User account expired." in driver.page_source) else "[FAIL]")
	elif i == 1: #UA02
		print("TEST 22: UA02 - Account Blocked Login"),
		inputCreds = driver.find_element_by_name("username")
		inputCreds.send_keys(username[i+1])
		inputCreds = driver.find_element_by_name("password")
		inputCreds.send_keys(pwd[2])
		inputCreds.submit()
		time.sleep(1)
		print("[PASS]" if ("User is blocked." in driver.page_source) else "[FAIL]")
	elif i == 2: #UA03
		print("TEST 23: UA03 - Account Password Change Login"),
		inputCreds = driver.find_element_by_name("username")
		inputCreds.send_keys(username[i+1])
		inputCreds = driver.find_element_by_name("password")
		inputCreds.send_keys(pwd[2])
		inputCreds.submit()
		time.sleep(1)
		print("[PASS]" if ("Change UA03's Password" in driver.page_source) else "[FAIL]")

		print("TEST 24: UA03 - Account Password Change Process"),
		InputInfo = driver.find_element_by_name("old_password")
		InputInfo.clear()
		InputInfo.send_keys(pwd[2])
		InputInfo = driver.find_element_by_name("password")
		InputInfo.clear()
		InputInfo.send_keys(pwd[3])
		InputInfo = driver.find_element_by_name("confirm_password")
		InputInfo.clear()
		InputInfo.send_keys(pwd[3])
		InputInfo.submit()
		time.sleep(1)
		print("[PASS]" if ("Successfully changed password." in driver.page_source) else "[FAIL]")
driver.get("http://localhost/otti_webtool/index.php/logout")

# Part D: Edit User Account

# Part E: Block/Unblock User Account

time.sleep(2)
driver.quit()