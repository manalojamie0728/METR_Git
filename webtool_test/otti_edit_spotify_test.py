from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("http://localhost/otti_webtool")

print "[[TEST II-2A: Edit OTT Product-Spotify]]"
# Initialize by Logging In First
InputCreds = driver.find_element_by_name("username")
InputCreds.send_keys("admin")
InputCreds = driver.find_element_by_name("password")
InputCreds.send_keys("admin")
InputCreds.submit()

time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_products/add")
InputInfo = driver.find_element_by_name("name")
InputInfo.send_keys("Spotify_004")
InputInfo = driver.find_element_by_name("keyword")
InputInfo.send_keys("spotify_004")
driver.find_element_by_xpath("//input[@name='endpoint_type'][@value='2']").click()
for m in range(0, 6):
	InputInfo = driver.find_element_by_name("params["+str(m)+"][value]")
	InputInfo.send_keys("foo")
InputInfo.submit()
time.sleep(1)
prod_id = driver.current_url.split('/')[-1]
driver.get("http://localhost/otti_webtool/index.php/ott_products/edit/"+prod_id)

name = ['', 'Spotify_005']
keyword = ['', 'spotify_005']
param = ['', 'new']

for i in range(0, 2):
	for j in range(0, 2):
		for k in range(0, 2):
			print("TEST "+str(4*i+2*j+k+1)+":"),
			InputInfo = driver.find_element_by_name("name")
			InputInfo.clear()
			InputInfo.send_keys(name[k])
			InputInfo = driver.find_element_by_name("keyword")
			InputInfo.clear()
			InputInfo.send_keys(keyword[j])
			for m in range(0, 6):
				InputInfo = driver.find_element_by_name("params["+str(m)+"][value]")
				InputInfo.clear()
				InputInfo.send_keys(param[i])
			InputInfo.submit()
			time.sleep(1)
			if (4*i+2*j+k+1) < 8:
				print("[PASS]" if not("Successfully updated OTT product." in driver.page_source) else "[FAIL]")
			else:
				print("[PASS]" if ("Successfully updated OTT product." in driver.page_source) else "[FAIL]")
time.sleep(1)
driver.get("http://localhost/otti_webtool/index.php/ott_products")

print("TEST 9: Check Edited Product In List"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if ("Spotify_005" in driver.page_source) else "[FAIL]")

print("TEST 10: Check Edited Product's Details"),
driver.get("http://localhost/otti_webtool/index.php/ott_products/details/"+prod_id)
time.sleep(1)
print("[PASS]" if ("Product Details" in driver.page_source) else "[FAIL]")

print("TEST 11: Delete Added Product From List"),
driver.get("http://localhost/otti_webtool/index.php/ott_products")
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
driver.get("http://localhost/otti_webtool/index.php/ott_products/delete/"+prod_id)
time.sleep(1)
print("[PASS]" if ("Successfully deleted OTT Product." in driver.page_source) else "[FAIL]")

print("TEST 12: Check Deletion Success"),
driver.find_element_by_id("dd_recsperpage").send_keys("50", Keys.ENTER)
time.sleep(1)
print("[PASS]" if not ("Spotify_005" in driver.page_source) else "[FAIL]")

#time.sleep(1)
#driver.find_element_by_xpath("//*[contains(text(), 'Add New Product')]").click()
time.sleep(3)
driver.quit()