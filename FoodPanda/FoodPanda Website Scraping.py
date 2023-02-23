#!/usr/bin/env python
# coding: utf-8

# #### Rules to follow for this script to run: --> (If you are using Jupyter Notebook)
# For downloading JupyterNotebook https://www.anaconda.com/products/distribution
# 1. To first run this code you have to press Shift + Enter or you can see Run button (Traingle) you can also press this. 
# 2. I have gave heading that this following code is for this website...
# 3. If you want to access the csv (excel file) then go on the location where you have imported your Jupyter Notebook
# 4. If you want the script to stop then click on the square button(Interrupting Kernal button)
# 5. Make sure that you have all files in one folder.
# ## Thank You!
# -----------------------------------------------------------------------------------

# # For foodpanda.my

# In[64]:


# download all these modules!
try:
    import csv
    import time
    import random
    import pandas as pd
    import pyautogui
except:
    print("Any Module is not download")

with open('FoodPandaScraper(foodpanda.my).csv', 'w', newline='',encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Email','Passowrd of Foodpanda','Password of gmail','recovery email'])
cnt = 0  
try:
    df = pd.read_excel("250 Gmail Pva Accounts (Order 6 Dec.xlsx")
    
    try:
        user = int(input("How many accounts do you want today? "))
        for i in range(user):
            # time.sleep(2)
           
            x, y = pyautogui.locateCenterOnScreen("ca.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            time.sleep(3) 
            pyautogui.typewrite("https://www.foodpanda.my/login/new?step=email")
            time.sleep(4)

            x, y = pyautogui.locateCenterOnScreen("Screenshot 2023-02-22 175430.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            time.sleep(7)

            try:
                x, y = pyautogui.locateCenterOnScreen("ca1.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(2)
            except:pass
            email_ = df["Email Address"][cnt]
            pyautogui.typewrite(email_)

            time.sleep(3)
            x, y = pyautogui.locateCenterOnScreen("ca4.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)

            time.sleep(4)

            x, y = pyautogui.locateCenterOnScreen("ca3.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)

            time.sleep(4)

            x, y = pyautogui.locateCenterOnScreen("ca.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            time.sleep(3)
            pyautogui.typewrite(f"https://www.foodpanda.my/login/new?action=verify-email&destination=registration&email={email_}&expiry=1677148798&verification-code=2x9Fx1f7Z33FGjqC")
            time.sleep(5)
            try:
                x, y = pyautogui.locateCenterOnScreen("ca8.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
            except:
                x, y = pyautogui.locateCenterOnScreen("ca81.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
            time.sleep(7)
            x, y = pyautogui.locateCenterOnScreen("ca5.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag")
            time.sleep(3)
            x, y = pyautogui.locateCenterOnScreen("ca51.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag")
            time.sleep(1.2)
            x, y = pyautogui.locateCenterOnScreen("ca52.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag1234")
            time.sleep(1.2)

            x, y = pyautogui.locateCenterOnScreen("ca6.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag1234")
            time.sleep(1.2)
            cnt += 1
            try:
                x, y = pyautogui.locateCenterOnScreen("ca7.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
#                 pyautogui.typewrite("Gag1234")
                time.sleep(1.2)
                x, y = pyautogui.locateCenterOnScreen("ca9.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(7)
                x, y = pyautogui.locateCenterOnScreen("ca6.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                pyautogui.typewrite("Gag1234")
            except:
                with open('FoodPandaScraper(foodpanda.my).csv', 'a', newline='',encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([email_,'Gag1234',password_,rec_email])

            time.sleep(1.2)
            
            
    except ValueError:
        print("Please input a number!")

except FileNotFoundError:
    print("Your file is unable to find!. Please check spelling and extension.")


# # For Foodpanda.sg

# In[59]:


# Imports
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

with open('FoodPandaScraper(foodpanda.sg).csv', 'w', newline='',encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Email','Passowrd of Foodpanda','Password of gmail','recovery email'])
cnt =0
try:
    df = pd.read_excel("250 Gmail Pva Accounts (Order 6 Dec.xlsx")
    
    try:
        user = int(input("How many accounts do you want today? "))
        for i in range(user):
            # time.sleep(2)
            
            try:
                x, y = pyautogui.locateCenterOnScreen("ca.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(3) 
                pyautogui.typewrite("https://www.foodpanda.sg/login/new?step=email")
                time.sleep(4)
            except:
                x, y = pyautogui.locateCenterOnScreen("caa1.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(3) 
                pyautogui.typewrite("https://www.foodpanda.sg/login/new?step=email")
                time.sleep(4)
                
            try:
                x, y = pyautogui.locateCenterOnScreen("food1.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(7)
            except:
                x, y = pyautogui.locateCenterOnScreen("caa2.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(7)

            try:
                x, y = pyautogui.locateCenterOnScreen("ca1.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(2)
            except:pass
            email_ = df["Email Address"][cnt]
            pyautogui.typewrite(email_)

            time.sleep(3)
            x, y = pyautogui.locateCenterOnScreen("ca4.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)

            time.sleep(4)

            x, y = pyautogui.locateCenterOnScreen("ca3.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)

            time.sleep(4)

            x, y = pyautogui.locateCenterOnScreen("ca.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            time.sleep(3)
            pyautogui.typewrite(f"https://www.foodpanda.sg/login/new?action=verify-email&destination=registration&email={email_}&expiry=1677148798&verification-code=2x9Fx1f7Z33FGjqC")
            time.sleep(5)
            try:
                x, y = pyautogui.locateCenterOnScreen("ca8.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
            except:
                x, y = pyautogui.locateCenterOnScreen("ca81.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
            time.sleep(7)
            x, y = pyautogui.locateCenterOnScreen("ca5.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag")
            time.sleep(3)
            x, y = pyautogui.locateCenterOnScreen("ca51.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag")
            time.sleep(1.2)
            x, y = pyautogui.locateCenterOnScreen("ca52.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag1234")
            time.sleep(1.2)

            x, y = pyautogui.locateCenterOnScreen("ca6.png", confidence=0.8)
            pyautogui.moveTo(x, y)
            #time.sleep(10)
            #x, y = pyautogui.position()
            pyautogui.click(interval=1)
            pyautogui.typewrite("Gag1234")
            time.sleep(1.2)
            cnt += 1
            try:
                x, y = pyautogui.locateCenterOnScreen("ca7.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                pyautogui.typewrite("Gag1234")
                time.sleep(1.2)
                x, y = pyautogui.locateCenterOnScreen("ca9.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                time.sleep(7)
                x, y = pyautogui.locateCenterOnScreen("ca6.png", confidence=0.8)
                pyautogui.moveTo(x, y)
                #time.sleep(10)
                #x, y = pyautogui.position()
                pyautogui.click(interval=1)
                pyautogui.typewrite("Gag1234")
            except:
                with open('FoodPandaScraper(foodpanda.sg).csv', 'a', newline='',encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([email_,'Gag1234',password_,rec_email])

            time.sleep(1.2)
            
            
            
            
    except ValueError:
        print("Please input a number!")

except FileNotFoundError:
    print("Your file is unable to find!. Please check spelling and extension.")


# In[ ]:




