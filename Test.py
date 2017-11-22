from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://www.youtube.com/results?search_query=" + "guitar+lessons")

# assert "guitar " in driver.title


time.sleep(5)
results = driver.find_elements_by_xpath('//*[@id="dismissable"]')

driver.close()

print(len(results))