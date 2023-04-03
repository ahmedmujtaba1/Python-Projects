import random
import undetected_chromedriver as uc 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from key_creating import generate_key

good_keys = 0
user = int(input("Enter how many times you want this script to check this keys? "))
def get_chrome():
    global driver
    
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    path = r'C:\Users\ABC\vpn1'
    chrome_options.add_argument(f'--load-extension={path}')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-popup-blocking')
    
    driver = uc.Chrome(options=chrome_options)
    curr=driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if handle != curr:
            driver.close()
    driver.switch_to.window(curr)
    driver.get("https://www.google.com/search?q=what+is+my+ip+address&ei")
    time.sleep(2)
    global main_ip
    try:
        main_ip = driver.find_element(By.XPATH,"//div[@style='padding-top:16px;padding-bottom:0px;padding-left:16px;padding-right:0px']//span//span").text
        print(f"Requesting with this ip Address : {main_ip}")
        driver.get("https://www.pidkeys.com/index/check/pid.html")
        time.sleep(7)
    except:pass   
main_ip = ''

def appl_visa():
    driver.get('chrome-extension://ebfdollnfpnidpbijmeljimeiglnnkgc/html/foreground.html')
    time.sleep(5)
    # time.sleep(4)
    title = 'VeePN'

    driver.find_element(By.CLASS_NAME,value='next').click()
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME,value='next').click()
    driver.find_element(By.CLASS_NAME,value='area-name').click()
    locations = ['//*[@id="region-list"]/div[2]/div[2]','//*[@id="region-list"]/div[3]','//*[@id="region-list"]/div[4]','//*[@id="region-list"]/div[5]','//*[@id="region-list"]/div[6]','//*[@id="region-list"]/div[7]']
    country = random.choice(locations)

    if country == '//*[@id="region-list"]/div[5]':
        driver.find_element(By.XPATH,value=country).click()
        number = random.randint(1,2)
        time.sleep(1)
        driver.find_element(By.XPATH,value= f'//*[@id="region-list"]/div[5]/div[2]/div/div[{number}]').click()    

    elif country=='//*[@id="region-list"]/div[7]':
        driver.find_element(By.XPATH,value=country).click()
        number = random.randint(1,3)
        time.sleep(1)
        driver.find_element(By.XPATH,value= f'//*[@id="region-list"]/div[7]/div[2]/div/div[{number}]').click()
    else:
        driver.find_element(By.XPATH,value= country).click()

    time.sleep(0.5)
    driver.find_element(By.ID,value="mainBtn").click()
    while True:
        time.sleep(5)
        if driver.find_element(By.XPATH,value='//*[@id="content"]/div[3]/div/div[2]/span[2]').text==main_ip:
            driver.find_element(By.ID,value="mainBtn").click()
        else:
            break

def final_scraper():
    key = generate_key()
    print("The key is ", key)
    driver.find_element(By.ID,"textarea_keys").clear()
    driver.find_element(By.ID,"textarea_keys").send_keys(key)
    time.sleep(1)
    try:
        driver.find_element(By.ID,"button_check").click()
        time.sleep(8)
    except:pass
    try:
        driver.find_element(By.XPATH,"//*[text()='Format error']")
            
        with open("output/block_list_keys.txt", "a") as file:
            file.write(f"{key} | ")
            file.close()
            # good_keys += 1
    
    except: 
        with open("output/working_keys.txt", "a") as file:
            file.write(f"{key} | ")
            file.close()

get_chrome()
time.sleep(1)
totalCount = 0
for i in range(user):
    if totalCount != 10:
        final_scraper()
        # print(f"Total {good_keys} working keys are collected")
        print("-----------------------------------------")
        totalCount += 1

        try:
            driver.find_element(By.XPATH,"//*[text()='Tourists can check up to 10 times every 24 hours']")
            appl_visa()
            totalCount = 0
            driver.get("https://www.google.com/search?q=what+is+my+ip+address&ei")
            time.sleep(2)
            main_ip = driver.find_element(By.XPATH,"//div[@style='padding-top:16px;padding-bottom:0px;padding-left:16px;padding-right:0px']//span//span").text
            print(f"Requesting with this ip Address : {main_ip}")
            driver.get("https://www.pidkeys.com/index/check/pid.html")
            time.sleep(7)
        except:pass
    else:
        appl_visa()
        totalCount = 0
        driver.get("https://www.google.com/search?q=what+is+my+ip+address&ei")
        time.sleep(2)
        main_ip = driver.find_element(By.XPATH,"//div[@style='padding-top:16px;padding-bottom:0px;padding-left:16px;padding-right:0px']//span//span").text
        print(f"Requesting with this ip Address : {main_ip}")
        driver.get("https://www.pidkeys.com/index/check/pid.html")
        time.sleep(7)
    # driver.quit()