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

print "[[TEST VII: User Activity Logs]] (Assumes you have done TEST VI beforehand)" # CLEAR!
actions = ['Unblock', 'Block', 'Reset Password']
pass_cycle = ['@dmIn123', 'M7Ght33Mou$e', 'H0jo$a7ok0', 'P@ric3$t4R', '0r4nGut@n', 'H@ppYMar74']
# Current Password: H0jo$a7ok0

# Initialize by Logging In First
Login(pass_cycle[2])
driver.get("http://localhost/otti_webtool/index.php/userlogs")

print("TEST 1: Apply Filter in Username - admin"),
InputInfo = driver.find_element_by_name("username")
InputInfo.clear()
InputInfo.send_keys("admin")
InputInfo.submit()
time.sleep(1)
data_txt = driver.find_element_by_name("username").get_attribute('value')
print("[PASS]" if (data_txt == "admin") else "[FAIL]")

for i in range(0, 3):
	print("TEST "+str(i*3+2)+": Assert Username = admin ("+str(i+1)+")"),
	data_txt = driver.find_element_by_xpath("//table/tbody/tr["+str(i+1)+"]/td[1]").text
	print("[PASS]" if (data_txt == "admin") else "[FAIL]")

	print("TEST "+str(i*3+3)+": Assert Section = User Accounts("+str(i+1)+")"),
	data_txt = driver.find_element_by_xpath("//table/tbody/tr["+str(i+1)+"]/td[2]").text
	print("[PASS]" if (data_txt == "User Accounts") else "[FAIL]")

	print("TEST "+str(i*3+4)+": Assert Action = "+actions[i]+" ("+str(i+1)+")"),
	data_txt = driver.find_element_by_xpath("//table/tbody/tr["+str(i+1)+"]/td[3]").text
	print("[PASS]" if (data_txt == actions[i]) else "[FAIL]")

time.sleep(2)
driver.quit()