try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    import undetected_chromedriver as uc
    import csv
    import time
except Exception as ex:
    print(ex)
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')

url = 'https://www.greenmangaming.com/games/destiny-2-lightfall-pc/'
driver = uc.Chrome(options=chrome_options)
driver.get(url)
time.sleep(7)
handling=driver.find_element(By.ID,"day").text
handling=handling.replace('n','')
handling=handling.replace('DD','')
handling=handling.replace(' ','')
# print(handling)
if len(handling) > 0:
    driver.find_element(By.ID,"day").send_keys("01")
    driver.find_element(By.ID,"month").send_keys("01")
    driver.find_element(By.ID,"year").send_keys("2000")
    driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
    time.sleep(2)
    print("[+] Successfully Done!")
    driver.quit()
else:
    print("[+] An error occured")

