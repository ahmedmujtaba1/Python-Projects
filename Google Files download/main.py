import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import result
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlsplit
from collections import deque
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import configparser
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

driver = uc.Chrome(options=chrome_options)
driver.maximize_window()
print(f"{bcolors.OKBLUE}[+] Hello, I am a Scraping bot {bcolors.ENDC}")
print("[+] Google Chrome has been opened.. Please keep it open")
df = pd.read_excel('google.xlsx')
fileTypes = ["xls","pdf", "kml","kmz","ppt","doc","rtf"]
words = ["Export","Import","Logistic","Supply Chain","Exim","Shipping","purchase","Procurement","Procuring","International trade","Cargo","Freight","Beneficial Cargo Owner (BCP)","Factory","Manufacturing Center"]
cnt = 0
no = 0
flag = True
for x in range(len(words)):
    keyword = df["Email ids from trainee to CEO of all countries extended ( 35 )"][x]
    final_word = str(words[x]) + keyword + "email ids"
    for v in range(len(df["In below countries / cities"])):
        country = df["In below countries / cities"][v]
        for n in range(len(fileTypes)):
            page = 0
            final_keyword = str(final_word) + str(country) + f"filetype:{fileTypes[n]}"
            print(f"[+] Searching for this keyword : {final_keyword}")
            driver.get(f"https://www.google.com/search?hl=en&as_q={final_keyword}")
            download_link_container = driver.find_elements(By.XPATH,"//span[@class='ZGwO7 s4H5Cf C0kchf NaCKVc yUTMj VDgVie']/../../../../../..//a")
            print(f"[+] There are {str(len(download_link_container))} results.")
            no = 0
            print("Page no : ", page)
            for c in range(len(download_link_container)+1):
                no += 1
                # print("Page no : ", page)
                if no == len(download_link_container):
                    page += 1
                    try:
                        driver.find_element(By.XPATH,"//*[text()='Next']").click()
                        time.sleep(5)
                    except:pass
                try:
                    # Switch to the new window
                    down_link = download_link_container[c].get_attribute("href")
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    print(f"[+] This is file link. {down_link}")
                    if "filetype:pdf" in final_keyword:
                        r = requests.get(down_link, stream=True)
                        cnt += 1
                        with open(f'./PDF Files/file{cnt}.pdf', 'wb') as f:
                            f.write(r.content)
                            print("[+] Downloaded pdf files in the folder of 'PDF Files'.")
                    else:
                        driver.get(down_link)
                    time.sleep(2)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    print("[+] Your Excel file is downloaded in your system Download Folder.")
                    print("--------------------------------------------------")
                except:pass
driver.quit()        