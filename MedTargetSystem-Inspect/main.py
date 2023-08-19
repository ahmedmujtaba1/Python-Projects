from selenium import webdriver
import undetected_chromedriver as uc
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}

url = "https://www.endocrine.org"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--auto-open-devtools-for-tabs')  
# chrome_options.add_argument('--enable-logging') 
driver = uc.Chrome(desired_capabilities=caps)
driver.maximize_window()
driver.get(url)
time.sleep(8)
logs = driver.get_log('performance')
with open("request.txt",'w',newline="") as f:
    f.write(str(logs))
# with open("urls.txt",'w',newline="") as f:
#     f.write("")
# Search for the "process" request payload
process_payload = None
cnt = 0
logs = str(logs)
logs = logs.replace('[','')
log_list = logs.split('https:')
for i in log_list:
    if "www" in i:
        i = i.split('}')
        i = i[0]
        i = i.replace('"','')
        i = i.split(',')
        i = i[0]
        j  = ""
        if "beacon" in str(i):
            j = i
            j = i.split('beacon')
            j = j[0]
            j = j.replace('/javascript','')
            j = j.replace('js','')
            j = str(j) + "beacon/process/"
            print("Finally get the url")
            with open("urls.txt",'a',newline="") as f:
                f.write("https:" + str(j) + "\n")
                break
        print("---------------------------------" + "\n")


           

