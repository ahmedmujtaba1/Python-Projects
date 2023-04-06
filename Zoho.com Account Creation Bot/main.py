import csv 
import requests
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


df = pd.read_csv('ayush_data.csv')
phone_number = ""
user = int(input("How much accounts do you want? "))
if user != int(len(df['Password'])) and user >= len(df['Password']):
    print("Please update your file also!")
else:
    for n in range(user):
        password = str(df["Password"][n])
        username = df["Username"][n]
        l_name = df["L_name"][n]
        f_name = df["F_name"][n]
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.zoho.com/mail/')
        # driver.get("https://sms-activation-service.com/en/home/")
        driver.implicitly_wait(50)

        driver.maximize_window()
        personal = driver.find_element(By.ID, 'personal')
        personal.click()
        # driver.implicitly_wait(50)
        time.sleep(5)

        email = driver.find_element(By.ID, 'username')
        email.send_keys(username)
        # driver.implicitly_wait(50)
        time.sleep(1)

        password = driver.find_element(By.ID, 'password')
        password.send_keys(password)
        # driver.implicitly_wait(50)
        time.sleep(1)

        fname = driver.find_element(By.ID, 'sfirstname')
        fname.send_keys(f_name)
        # driver.implicitly_wait(50)
        time.sleep(1)

        lname = driver.find_element(By.ID, 'lastname')
        lname.send_keys(l_name)
        driver.implicitly_wait(50)

        number = driver.find_element(By.ID, 'mobile')
        number.send_keys(phone_number)
        driver.implicitly_wait(50)

        re_number = driver.find_element(By.ID, 'confirmMobile')
        re_number.send_keys(phone_number)
        driver.implicitly_wait(50)

        check = driver.find_element(By.ID, 'tos')
        check.click()
        driver.implicitly_wait(50)

        submit = driver.find_element(By.ID, 'signupbtn')
        submit.click()       
        driver.implicitly_wait(50)

        #otp = driver.find_element(By.ID, 'optfield')
        #otp.send_keys()

        #verify = driver.find_element(By.NAME, 'optfield')
        #verify.click()
        #driver.implicitly_wait(50) 

        time.sleep(50)


        driver.quit()