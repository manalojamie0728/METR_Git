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

print "[[TEST VIII: Webtool Settings]]"
schema_assert = [5, 8, 30, 5, 180, 1, 1, 1, 1, 1]
new_vals = [3, 10, 15, 1, 120, 2, 2, 2, 2, 2]
assert_case = ['Max Password Retry Count', 'Min Password Length', 'Password Expiry', 'Password No Reuse',
			'Session Timeout', 'Password Expiry Warning', 'Min Uppercase Chars', 'Min Lowercase Chars',
			'Min Numeric Chars', 'Min Special Chars', '(Correct Values)']
field_names = ['MAX_PASSWORD_RETRY_COUNT', 'MIN_PASSWORD_LENGTH', 'PASSWORD_EXPIRY_DAYS', 'PASSWORD_NOREUSE_COUNT',
			'SESSION_TIMEOUT_MINUTES', 'PASSWORD_EXPIRY_WARNING_DAYS', 'PASSWORD_MIN_ALPHA_UCASE_COUNT',
			'PASSWORD_MIN_ALPHA_LCASE_COUNT', 'PASSWORD_MIN_DIGIT_COUNT', 'PASSWORD_MIN_SPECIAL_COUNT']
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: M7Ght33Mou$e

# Initialize by Logging In First
Login(pass_cycle[1])
driver.get("http://localhost/otti_webtool/index.php/settings/webtool_settings")

# Part A: Assertion of Present Values
for i in range(0, 10):
	print("TEST "+str(i+1)+": Assert "+assert_case[i]),
	data_txt = driver.find_element_by_name(field_names[i]).get_attribute('value')
	print("[PASS]" if (data_txt == str(schema_assert[i])) else "[FAIL]")

# Part B: Update Webtool Settings
for i in range(0, 11):
	print("TEST "+str(i+11)+": Update "+assert_case[i]),
	for j in range(0, 10):
		InputInfo = driver.find_element_by_name(field_names[j])
		InputInfo.clear()
		InputInfo.send_keys(new_vals[j])
	if i < 10:
		driver.find_element_by_name(field_names[i]).clear()
	InputInfo.submit()
	time.sleep(1)
	print("[PASS]" if not ("Successfully saved webtool settings." in driver.page_source) else "[FAIL]")

# Part C: Assertion of Updated Values
for i in range(0, 10):
	print("TEST "+str(i+22)+": Assert "+assert_case[i]),
	data_txt = driver.find_element_by_name(field_names[i]).get_attribute('value')
	print("[PASS]" if (data_txt == str(new_vals[i])) else "[FAIL]")

# Part D: Revert Webtool Settings
InputInfo = driver.find_element_by_name(field_names[0])
for i in range(0, 10):
	InputInfo = driver.find_element_by_name(field_names[i])
	InputInfo.clear()
	InputInfo.send_keys(schema_assert[i])
InputInfo.submit()
time.sleep(1)

time.sleep(2)
driver.quit()