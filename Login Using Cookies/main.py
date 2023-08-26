from selenium import webdriver
import time, pickle

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://instagram.com/')
print("Login please and make sure the page is reloaded.")
user = input("Are you done? : ")
cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

driver.quit()
# --------------------------------------------------
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://instagram.com/')
with open('cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(50000)