#!/usr/bin/env python
# coding: utf-8

# In[37]:


import names
import random
import undetected_chromedriver as uc 
import time
import string
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui
from PIL import Image
from selenium.webdriver.common.keys import Keys

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-popup-blocking')

driver = uc.Chrome(options=chrome_options)
driver.get("https://web.whatsapp.com/")
print('[+] Scan Your QR Code')
actions = ActionChains(driver)
time.sleep(80)


# In[40]:



driver.switch_to.window(driver.window_handles[0])  
try:
    message_from_user = driver.find_element(By.XPATH,f"(//span[@data-testid='icon-unread-count'])[1]")
    message_from_user.click()
except Exception as ex:
    print(ex)


try:
    message_from_user = driver.find_element(By.XPATH,"(//span[@aria-label='1 unread message'])[1]")
except:
    try:
        message_from_user = driver.find_element(By.XPATH,"(//span[@aria-label='1 unread message'])[1]")
        message_from_user.click()
    except:pass
driver.switch_to.window(driver.window_handles[0])  
print('[+] Successfully Recieved the message!')
bot = driver.find_element(By.XPATH,"//p[@class='selectable-text copyable-text iq0m558w']")
message = "Do you want to talk with human or bot?"
bot.send_keys(message)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(20)
title = driver.find_element(By.XPATH,"//span[@data-testid='conversation-info-header-chat-title']").text
messages = driver.find_elements(By.XPATH,f"//span[@aria-label='{title}:']/..//div//div//span//span")
userd = messages[len(messages)-3].text
# print(userd)
if "human" in userd or "Human" in userd:
    driver.quit()
     
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
message = "Hey, I am bot.... Please can you provide me such details : email"
bot.send_keys(message)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
message = " Please provide data like \nEmail :?"
# print(message)
bot.send_keys(message)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
text = messages[len(messages)-3].text
if text == "EXIT":
    driver.quit()
# ad_title
print('[+] Successfully Send message!')
time.sleep(8)
driver.find_element(By.XPATH,"//header[@data-testid='conversation-header']").click()
time.sleep(2)
contact = driver.find_element(By.XPATH,"//span[@class='enbbiyaj e1gr2w1z pm5hny62']").text
driver.find_element(By.XPATH,"//div[@data-testid='btn-closer-drawer']").click()
time.sleep(5)

time.sleep(8)
email = []
for i in driver.find_elements(By.XPATH,"//div[@class='copyable-text']"):
    try:
        alls = i.text
#         print(i.text)
    except:pass
#         alls = "ahmedmjddj@gmail.com"

    if "@" in alls:
        email_ = alls
    uu=alls.split(" ")
    for i in uu:
        email_ = i
#     print(email_)    

print(email_)

username_list = email_.split("@")
username = username_list[0]
password = "1234"
print("[+] Successfully get the data!")
print("Email : ", email_)
print("Contact Number : ", contact)
print("UserName : ", username)
print("Password : ", password)


time.sleep(5)
driver.execute_script("window.open('https://jatalog.com/registerm/');")
# Switch to the new window
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
try:
    driver.find_element(By.ID,"pwbox-1798").send_keys(1234)
    driver.find_element(By.XPATH,"//input[@name='Submit']").click()
except:pass

time.sleep(5)
driver.find_element(By.ID,"sb_reg_name").send_keys(username)
driver.find_element(By.ID,"adforest_contact_number").send_keys(contact)
driver.find_element(By.ID,"sb_reg_email").send_keys(email_)
driver.find_element(By.ID,"sb_reg_password").send_keys(password) 
driver.find_element(By.XPATH,"//input[@name='sb_reg_password_confirm']").send_keys(password)
time.sleep(2)
a = driver.find_element(By.XPATH,"//div[@class='icheckbox_minimal']//ins")
driver.execute_script("arguments[0].scrollIntoView();", a)
a.click() 
time.sleep(1.2)
b = driver.find_element(By.XPATH,"(//*[text()='Register'])[2]")
driver.execute_script("arguments[0].scrollIntoView();", b)
time.sleep(1.2)
b.click()
try:
    b.click()
except:pass

time.sleep(10)
try:
    driver.find_element(By.ID,"role_as_vendor")
except:pass
print('[+] Successfully Registered!')
time.sleep(8)
driver.get("https://jatalog.com/ad-post/")
time.sleep(8)

# driver.switch_to.window(driver.window_handles[0])
try:
    driver.find_element(By.ID,"sb_reg_email")
    message = "Opps, Your provided details are already registered!"
    time.sleep(2)
    driver.find_element(By.ID,"sb_reg_email").send_keys(email_)
    driver.find_element(By.XPATH,"//input[@name='sb_reg_password']").send_keys("1234")
    time.sleep(2)
    driver.find_element(By.ID,"sb_login_submit").click()
    time.sleep(4)
    
except:
    message = "Congratulations! Your account has been created!"
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
# message = "Congratulations! Your account has been created!"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(15)
text = messages[len(messages)-3].text
if text == "EXIT":
    driver.quit()
# ad_title
time.sleep(1)
message = "Please provide data for posting ad!"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
time.sleep(1)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
message = "I want Ad Title"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
time.sleep(1)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(20)
title = driver.find_element(By.XPATH,"//span[@data-testid='conversation-info-header-chat-title']").text
messages = driver.find_elements(By.XPATH,f"//span[@aria-label='{title}:']/..//div//div//span//span")
ad_title = messages[len(messages)-3].text
text = messages[len(messages)-3].text
if text == "EXIT":
    driver.quit()
# ad_title
#                 -------------------------------------------------------
message = "I want Ad Description"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
time.sleep(1)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(25)
title = driver.find_element(By.XPATH,"//span[@data-testid='conversation-info-header-chat-title']").text
messages = driver.find_elements(By.XPATH,f"//span[@aria-label='{title}:']/..//div//div//span//span")
ad_description = messages[len(messages)-3].text
text = messages[len(messages)-3].text
if text == "EXIT":
    driver.quit()
# ad_title
#                                   -----------------------------
message = "I want Ad Price"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
time.sleep(1)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(15)
title = driver.find_element(By.XPATH,"//span[@data-testid='conversation-info-header-chat-title']").text
messages = driver.find_elements(By.XPATH,f"//span[@aria-label='{title}:']/..//div//div//span//span")
ad_price = messages[len(messages)-3].text
# ad_title
text = messages[len(messages)-3].text
if text == "EXIT":
    driver.quit()
# ad_title
# print(ad_title, ad_description, ad_price)

#           --------------------------------------------------------      -------------
message = "I want Ad Location"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
time.sleep(1)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(15)
title = driver.find_element(By.XPATH,"//span[@data-testid='conversation-info-header-chat-title']").text
messages = driver.find_elements(By.XPATH,f"//span[@aria-label='{title}:']/..//div//div//span//span")
ad_location = messages[len(messages)-3].text

text = messages[len(messages)-3].text
if text == "EXIT":
    driver.quit()
# ad_title
#  ------------------------        -------------------------------------------
message = "I want Ad Category Select from one Animals, Electronics, Fashion & Beauty, Garden & Outdoor, Jobs, Other Items, Real Estate, Services, Vehicles"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
time.sleep(1)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(26)
title = driver.find_element(By.XPATH,"//span[@data-testid='conversation-info-header-chat-title']").text
messages = driver.find_elements(By.XPATH,f"//span[@aria-label='{title}:']/..//div//div//span//span")
ad_category_user = messages[len(messages)-3].text
if "Animals" in ad_category_user or "animals" in ad_category_user or "animal" in ad_category_user or "Animal" in ad_category_user:
    ad_category = "Animals"
elif "Electronics" in ad_category_user or "electronics" in ad_category_user or "electronic" in ad_category_user or "Electronic" in ad_category_user:
    ad_category = "Electronics"
elif "Services" in ad_category_user or "services" in ad_category_user or "service" in ad_category_user or "Service" in ad_category_user:
    ad_category = "Services"
    
elif "Fashion & Beauty" in ad_category_user or "Fashion" in ad_category_user or "Fashion and Beauty" in ad_category_user or "Beauty" in ad_category_user or "fashion" in ad_category_user or "beauty" in ad_category_user:
    ad_category = "Fashion & Beauty"
    
elif "Jobs" in ad_category_user or "jobs" in ad_category_user or "job" in ad_category_user or "Job" in ad_category_user:
    ad_category = "Jobs"
    
elif "Other Items" in ad_category_user or "other items" in ad_category_user or "other" in ad_category_user or "Other items" in ad_category_user or "Other Items" in ad_category_user or "items" in ad_category_user or "other Items" in ad_category_user:
    ad_category = "Other Items"

elif "Real Estate" in ad_category_user or "real" in ad_category_user or "real estate" in ad_category_user or "Real estate" in ad_category_user or "estate" in ad_category_user or "Real" in ad_category_user or "Estate" in ad_category_user:
    ad_category = "Real Estate"

elif "Vehicles" in ad_category_user or "vehicles" in ad_category_user or "Vehicle" in ad_category_user or "vehicle" in ad_category_user:
    ad_category = "Vehicles"

elif "Garden & Outdoor" in ad_category_user or "Garden" in ad_category_user or "garden" in ad_category_user or "Outdoor" in ad_category_user or "Garden and Outdoor":
    ad_category = "Garden & Outdoor"

time.sleep(2)
print(ad_category)
    # ad_title
# print(ad_title, ad_description, ad_price)
#  ------------------------------------------                           --------------------------------------
message = "I want Ad Images"
bot = driver.find_element(By.XPATH,"//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
bot.send_keys(message)
time.sleep(1)
send_message = driver.find_element(By.XPATH,"//button[@data-testid='compose-btn-send']")
send_message.click()
time.sleep(27)
print("[+] Ad Details Provided by User: ")
print('Ad Title : ', ad_title)
print('Ad Description : ', ad_description)
print('Ad price : ', ad_price)
print('Ad Location : ', ad_location)
print('Ad Category : ', ad_category)     
driver.switch_to.window(driver.window_handles[0])
time.sleep(15)
lish = driver.find_elements(By.XPATH,"//div[@data-testid='media-url-provider']//div[2]//img")
# print(lish)
cnt = 0
for h in range(len(lish)):
    cnt += 1

element = driver.find_element(By.XPATH,f"(//div[@data-testid='media-url-provider']//div[2]//img)[{cnt}]")

location = element.location
size = element.size

driver.save_screenshot("shot.png")

x = location['x']
y = location['y']
w = size['width']
h = size['height']
width = x + w
height = y + h

im = Image.open('shot.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('image.png')
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.find_element(By.XPATH,"//span[@class='select2-selection__arrow']").click()
time.sleep(1)
#             ad_title = "Jobs"
#     driver.switch_to.window(driver.window_handles[1])
#     time.sleep(5)
try:
    driver.find_element(By.XPATH,f"(//*[text()='{ad_category}'])[3]").click()
except:
    print('Invalid Input!')
time.sleep(3)
driver.find_element(By.XPATH,"//*[text()='Next']").click()
time.sleep(2)

#             ad_title = "Pagal BAcho"
#             ad_price = '029'
driver.find_element(By.ID,"ad_title").send_keys(ad_title)
driver.find_element(By.XPATH,"//*[text()='Buy']").click()
#             ad_description = "jl0joi7gytoi"
driver.find_element(By.XPATH,"//div[@class='jqte_editor']").send_keys(ad_description)
price_holder = driver.find_element(By.ID,"ad_price")
driver.execute_script("arguments[0].scrollIntoView();", price_holder)
price_holder.send_keys(ad_price)
time.sleep(5)
from selenium.webdriver.common.keys import Keys
driver.find_element(By.XPATH,"//body").send_keys(Keys.PAGE_DOWN)
time.sleep(5)
actions = ActionChains(driver)
element_present = driver.find_element(By.XPATH, "//div[@class='dz-default dz-message']")
try:
    actions.move_to_element(element_present).click().perform()
except:pass
#     driver.findelement(By.XPATH,"//body").send_keys(Keys.PAGE_UP)
# driver.execute_script("arguments[0].scrollIntoView();", element_present)
time.sleep(2)
# element_present.click()
time.sleep(2)
pyautogui.write(r'C:\Users\ABC\Whatsapp Automation\image.png')#your path
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.write(r'C:\Users\ABC\Whatsapp Automation\image.png')#your path
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)

kk = driver.find_element(By.XPATH,"(//span[@class='select2-selection__arrow'])[7]")

try:
    actions.move_to_element(kk).click().perform()
except:pass
c = driver.find_element(By.XPATH,"(//*[text()='OK'])[2]")
driver.execute_script("arguments[0].scrollIntoView();", c)
c.click()
#     actions.move_to_element(c).click().perform()
try:
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView();", kk)
    kk.click()
except:pass

time.sleep(5)
ad_title = "Kingston"
try:
    driver.find_element(By.XPATH,f"(//*[text()='{ad_title}'])[1]").click()
except:
    print('Invalid Input!')
time.sleep(5)
ad_title = "Kingston"
try:
    driver.find_element(By.XPATH,f"(//*[text()='{ad_title}'])[1]").click()
except:
    print('Invalid Input!')

time.sleep(2)
driver.find_element(By.ID,"sb_user_address").send_keys(ad_location)

time.sleep(2)

time.sleep(1)
driver.find_element(By.XPATH,"//body").send_keys(Keys.PAGE_DOWN)
time.sleep(3)
try:
    a = driver.find_element(By.XPATH,"//div[@class='icheckbox_minimal']//ins")
    driver.execute_script("arguments[0].scrollIntoView();", a)
    a.click()
except:
    try:
        a = driver.find_element(By.XPATH,"//div[@class='icheckbox_minimal parsley-error']//ins")
        driver.execute_script("arguments[0].scrollIntoView();", a)
        a.click()
    except:pass
time.sleep(1.2)

a = driver.find_element(By.XPATH,"//div[@class='submit-button']//input")
driver.execute_script("arguments[0].scrollIntoView();", a)
time.sleep(2)
a.click() 
time.sleep(1.2)
print('[+] Successfully Added Ad')


# In[ ]:




