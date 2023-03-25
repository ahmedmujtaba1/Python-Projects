#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import telebot

# Initialize Telegram bot
bot = telebot.TeleBot("5864971354:AAFfjYb_DcZ36AfZhvS9s266YDoFSnMr8EU")

# Define your chat ID
chat_id = "5583390542"

options = ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = Chrome(options=options)

def click_element(driver, element_xpath):
    try:
        element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
        element.click()
        print('Successfully clicked the element.')
        return True
    except Exception as e:
        print(f'Failed to click the element: {e}')
        return False

def navigate_to_page(driver, url):
    try:
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        print('Successfully navigated to the page.')
        return True
    except Exception as e:
        print(f'Failed to navigate to the page: {e}')
        return False

def get_balance(driver):
    try:
        balance_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@data-cy='value']")))
        balance = balance_element.text
        return balance
    except Exception as e:
        print(f'Failed to get balance: {e}')
        return None

def main():
    navigate_to_page(driver, 'https://hypedrop.com')
    input('Press ENTER to continue...')
    
    while True:
        navigate_to_page(driver, 'https://www.hypedrop.com/en/eu/rewards/daily')
        
        for i in range(7):
            try:
                time.sleep(2)
                driver.find_element(By.ID,"mat-input-0").send_keys("chistinanadia458@gmail.com")
                driver.find_element(By.ID,"mat-input-1").send_keys("myhappyfamily12")
                driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator flex-1 mat-flat-button mat-button-base mat-accent']").click()
                time.sleep(2)

                time.sleep(random.randint(5, 10))
                balance = get_balance(driver)
                if balance is not None:
                    message = f"Your balance is {balance}."
                else: 
                    message = "Failed to get balance."
                print(message)
                bot.send_message(chat_id, message)
                wait_time = random.randint(61, 3601)
                print(f'Waiting for {wait_time} seconds before trying again...')
                time.sleep(wait_time)
            except Exception as e:
                print(f'An error occurred while trying to click the element: {e}')
                driver.refresh()

        print('Waiting for 24 hours before trying again...')
        time.sleep(86400)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        driver.quit()


# In[ ]:





# In[ ]:




