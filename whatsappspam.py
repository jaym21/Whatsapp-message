from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#setting the webdriver to Chrome browser
driver = webdriver.Chrome()

#setting the driver to open whatsapp website
driver.get('https://web.whatsapp.com')

#as whatsapp web requires a QR code to enter the account so we need to stop the code and let the user to enter QR code and then continue
input('Enter the QR code then enter any key')

name = input('Enter the name of receiver: ')
#using css selector to select the receivers chat name 
receiver = driver.find_element_by_css_selector("span[title='"+ name +"']")
#now to enter the chat of reciever
receiver.click()

#to set after how much time should the message be delivered
time.sleep(10) #time.sleep() takes input in seconds so to set time as 3 hours: 3*60*60

#taking form user the receivers chat textbox's xpath 
xPath = input('Enter the xpath of the recievers chat textbox: ')
#setting this xpath to textinput
textinput = driver.find_element_by_xpath(xPath)

#for loop can be added to send spam the same message multiple times
# for i in range(10):
#entering the message to be sent
textinput.send_keys("Hi")
#this line will send the message
textinput.send_keys(Keys.RETURN)