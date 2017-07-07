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

print "[[TEST II-A: Add/Edit OTT Product-Spotify]]" # CLEAR! ***
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: H0jo$a7ok0

# Initialize by Logging In First
Login(pass_cycle[2])

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_products/add")

name = ['', 'Spotify_003', 'Spotify_004']
keyword = ['', 'spotify_003', 'spotify_004']
param = ['', 'foo', 'noo']
test_cases = ['Missing Name', 'Missing Keyword', 'Missing Endpoint', 'Missing Params', 'Complete Details']

# Part A: Add Spotify Product
print("TEST 1: Check Product Existence"),
InputInfo = driver.find_element_by_name("name")
InputInfo.clear()
InputInfo.send_keys('Spotify_001')
InputInfo = driver.find_element_by_name("keyword")
InputInfo.clear()
InputInfo.send_keys('spotify_001')
InputInfo.submit()
time.sleep(1)
print("[PASS]" if ("This Name is already taken." in driver.page_source) else "[FAIL]")

for i in range(0, 5):
	print("TEST "+str(i+2)+": "+test_cases[i]),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys(name[1])
	InputInfo = driver.find_element_by_name("keyword")
	InputInfo.clear()
	InputInfo.send_keys(keyword[1])
	if i > 2:
		driver.find_element_by_xpath("//input[@name='endpoint_type'][@value='2']").click()
		if i == 4:
			for m in range(0, 6):
				InputInfo = driver.find_element_by_name("params["+str(m)+"][value]")
				InputInfo.clear()
				InputInfo.send_keys(param[1])
	if i == 0:
		driver.find_element_by_name("name").clear()
	elif i == 1:
		driver.find_element_by_name("keyword").clear()
	InputInfo.submit()
	time.sleep(1)
	if (i+2) < 6:
		print("[PASS]" if not("Successfully created OTT product." in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully created OTT product." in driver.page_source) else "[FAIL]")

time.sleep(1)
prod_id = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_products")

print("TEST 7: Check Added Product In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("Spotify_003" in driver.page_source) else "[FAIL]")

print("TEST 8: Check Added Product's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_products/details/"+prod_id)
time.sleep(1)
print("[PASS]" if ("Product Details" in driver.page_source) else "[FAIL]")

# Part B: Edit Spotify Product
driver.get("http://localhost/otti_webtool/index.php/ott_products/edit/"+prod_id)
test_cases.pop(2) # Remove 
for i in range(0, 4):
	print("TEST "+str(i+9)+": "+test_cases[i]),
	InputInfo = driver.find_element_by_name("name")
	InputInfo.clear()
	InputInfo.send_keys(name[2])
	InputInfo = driver.find_element_by_name("keyword")
	InputInfo.clear()
	InputInfo.send_keys(keyword[2])
	for m in range(0, 6):
		InputInfo = driver.find_element_by_name("params["+str(m)+"][value]")
		InputInfo.clear()
		InputInfo.send_keys(param[2])
	if i == 0:
		driver.find_element_by_name("name").clear()
	elif i == 1:
		driver.find_element_by_name("keyword").clear()
	elif i == 2:
		for m in range(0, 6):
			driver.find_element_by_name("params["+str(m)+"][value]").clear()
	InputInfo.submit()
	time.sleep(1)
	if (i+1) < 4:
		print("[PASS]" if not("Successfully updated OTT product" in driver.page_source) else "[FAIL]")
	else:
		print("[PASS]" if ("Successfully updated OTT product" in driver.page_source) else "[FAIL]")

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_products")

print("TEST 13: Check Edited Product In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("Spotify_004" in driver.page_source) else "[FAIL]")

print("TEST 14: Check Edited Product's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_products/details/"+prod_id)
time.sleep(1)
print("[PASS]" if ("Product Details" in driver.page_source) else "[FAIL]")

# Part C: Delete Spotify Product
print("TEST 15: Delete Added Product From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_products")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_products/delete/"+prod_id)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT Product." in driver.page_source) else "[FAIL]")

print("TEST 16: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("Spotify_004" in driver.page_source) else "[FAIL]")

time.sleep(2)
driver.quit()