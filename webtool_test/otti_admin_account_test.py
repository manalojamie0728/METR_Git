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

print "[[TEST IV: Admin Account Page]]"
name = ['', 'METR Admin']
email = ['', 'metr.com', 'metr.emailadd@metr.com.ph']
new_pwd = ['', 'Matsuri', 'PuyoPuy0', 'P@ric3$t4R']
curr_pwd = ['', 'admin', 'H0jo$a7ok0']
test_cases = ['Blank Admin/Blank Email', 'Blank Admin/Wrong Email', 'Blank Admin/Correct Email',
				'Filled Admin/Blank Email', 'Filled Admin/Wrong Email', 'Filled Admin/Correct Email']
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: H0jo$a7ok0

# Initialize by Logging In First
Login(pass_cycle[2])

# Part A: Edit Account Details
for i in range(0, 2):
	driver.get("http://localhost/otti_webtool/index.php/me")
	for j in range(0, 3):
		print("TEST "+str(3*i+j+1)+": "+test_cases[3*i+j]),
		InputCreds = driver.find_element_by_name("fullname")
		InputCreds.clear()
		InputCreds.send_keys(name[i])
		InputCreds = driver.find_element_by_name("email")
		InputCreds.clear()
		InputCreds.send_keys(email[j])
		InputCreds.submit()
		time.sleep(1)
		if (3*i+j+1)%3 != 0:
			print("[PASS]" if not ("Successfully updated user account." in driver.page_source) else "[FAIL]")
		else:
			print("[PASS]" if ("Successfully updated user account." in driver.page_source) else "[FAIL]")

# Part B: Change Password
driver.get("http://localhost/otti_webtool/index.php/me/change_password")
for i in range(0, 3):
	for j in range(0, 4):
		for k in range(0, 4):
			print("TEST "+str(16*i+4*j+k+7)+": Password Test"),
			InputInfo = driver.find_element_by_name("old_password")
			InputInfo.clear()
			InputInfo.send_keys(curr_pwd[i])
			InputInfo = driver.find_element_by_name("password")
			InputInfo.clear()
			InputInfo.send_keys(new_pwd[k])
			InputInfo = driver.find_element_by_name("confirm_password")
			InputInfo.clear()
			InputInfo.send_keys(new_pwd[j])
			InputInfo.submit()
			time.sleep(1)
			if (16*i+4*j+k+7) < 54:
				print("[PASS]" if not ("Successfully" in driver.page_source) else "[FAIL]")
			else:
				print("[PASS]" if ("Successfully" in driver.page_source) else "[FAIL]")

time.sleep(2)
driver.quit()