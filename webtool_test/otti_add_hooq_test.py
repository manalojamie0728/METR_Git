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

print "[[TEST II-1B: Add OTT Product-Hooq]]" # CLEAR!
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: H0jo$a7ok0

# Initialize by Logging In First
Login(pass_cycle[2])

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_products/add")

name = ['', 'Hooq_003']
keyword = ['', 'hooq_003']
param = ['', 'foo']

print("TEST 1: Check Product Existence"),
InputInfo = driver.find_element_by_name("name")
InputInfo.clear()
InputInfo.send_keys('Hooq_001')
InputInfo = driver.find_element_by_name("keyword")
InputInfo.clear()
InputInfo.send_keys('hooq_001')
InputInfo.submit()
time.sleep(1)
print("[PASS]" if ("This Name is already taken." in driver.page_source) else "[FAIL]")

for i in range(0, 2):
	for j in range(0, 2):
		for k in range(0, 2):
			for l in range(0, 2):
				print("TEST "+str(8*i+4*j+2*k+l+2)+":"),
				InputInfo = driver.find_element_by_name("name")
				InputInfo.clear()
				InputInfo.send_keys(name[l])
				InputInfo = driver.find_element_by_name("keyword")
				InputInfo.clear()
				InputInfo.send_keys(keyword[k])
				if j == 1:
					driver.find_element_by_xpath("//input[@name='endpoint_type'][@value='3']").click()
					for m in range(0, 4):
						InputInfo = driver.find_element_by_name("params["+str(m)+"][value]")
						InputInfo.clear()
						InputInfo.send_keys(param[i])
				InputInfo.submit()
				time.sleep(1)
				if (8*i+4*j+2*k+l+1) < 16:
					print("[PASS]" if not("Successfully created OTT product." in driver.page_source) else "[FAIL]")
				else:
					print("[PASS]" if ("Successfully created OTT product." in driver.page_source) else "[FAIL]")
time.sleep(1)
prod_id = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_products")

print("TEST 18: Check Added Product In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("Hooq_003" in driver.page_source) else "[FAIL]")

print("TEST 19: Check Added Product's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_products/details/"+prod_id)
time.sleep(1)
print("[PASS]" if ("Product Details" in driver.page_source) else "[FAIL]")

print("TEST 20: Delete Added Product From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_products")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_products/delete/"+prod_id)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT Product." in driver.page_source) else "[FAIL]")

print("TEST 21: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("Hooq_003" in driver.page_source) else "[FAIL]")

time.sleep(3)
driver.quit()