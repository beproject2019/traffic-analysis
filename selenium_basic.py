from selenium import webdriver

driver =webdriver.Firefox()
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# extract particular data based on its Xpath
buyer=driver.find_elements_by_xpath('//div[@title="buyer-name"]') 
price=driver.find_elements_by_xpath('//span[@class="item-price"]')

num_indexes=len(buyer) 
for i in range (num_indexes):
	print(buyer[i].text + "  : " + price[i].text)

driver.close()	