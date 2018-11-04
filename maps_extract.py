from selenium import webdriver
from time import sleep
import os.path
import time
import datetime
driver =webdriver.Chrome(executable_path=r'C:/Users/Pathak/Downloads/chromedriver_win32/chromedriver.exe')
counter=0
while True  :
	

	driver.get("https://www.google.co.in/maps/@18.9967228,73.118955,21z/data=!5m1!1e1?hl=en&authuser=0")
	start='C://Users//Pathak//Downloads//chromedriver_win32'
	df=str(counter);
	gh=str(time.time())

	ft=df+gh+'.png'
	final=os.path.join(start,ft)
	driver.get_screenshot_as_file(final) 
	counter+=1
	
	sleep(20)

driver.quit()
