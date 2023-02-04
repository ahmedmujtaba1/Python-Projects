import random
import undetected_chromedriver as uc 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import pyautogui
import time
from playsound import playsound
# time.sleep(2)

df = pd.read_excel("Information.xlsx")
time.sleep
number_list = [1,2,3]

ra = random.choice(number_list)
global cnt
cnt = 0
tries = 0
def get_chrome():
    global driver
    
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    path = r'C:\Users\ABC\vpn1'
    chrome_options.add_argument(f'--load-extension={path}')

#    chrome_options.add_argument('--load-extension=C:/Users/ABC/Downloads/Ahmed Task/proxy_auth_plugin')
#     chrome_options.add_argument('--proxy-server=%s' % proxy)
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-popup-blocking')
    
    driver = uc.Chrome(options=chrome_options)

    url = "https://visa.vfsglobal.com/ind/en/ltu/login"

    number_list = [1,2,3]

    ra = random.choice(number_list)

    main_ip = '49.43.73.81'

    driver.get('chrome-extension://ebfdollnfpnidpbijmeljimeiglnnkgc/html/foreground.html')
    time.sleep(5)
    curr=driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if handle != curr:
            driver.close()
    driver.switch_to.window(curr)
    time.sleep(4)
    title = 'VeePN'
    # maximize(title)
#     check = pyautogui.getWindowsWithTitle(title)
#     check[0].maximize()
#     print(check)

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


    driver.get("https://visa.vfsglobal.com/ind/en/ltu/login") 

    time.sleep(5)
    curr=driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if handle != curr:
            driver.close()
    driver.switch_to.window(curr)

    time.sleep(2)
def login_username(email_):
    wait.until(EC.presence_of_element_located((By.XPATH, f"//input[@placeholder='jane.doe@email.com']"))).send_keys(email_)
    time.sleep(1)

def login_password(pw):
    passw_input = driver.find_element(By.XPATH,"//input[@formcontrolname='password']")
    passw_input.send_keys(pw)
    time.sleep(2)
    
def login():
    driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator btn mat-btn-lg btn-block btn-brand-orange mat-stroked-button mat-button-base ng-star-inserted']").click()
    time.sleep(5)
    
num = 0
def visa_application(num=num, cnt=cnt):  #
    from selenium.webdriver.common.keys import Keys

    if df["Appointment"][num]=='all':
        listof = [" Lithuania Visa Application Center - Bangalore ",
        " Lithuania Visa Application Center - Chennai ",
        " Lithuania Visa Application Center - Delhi ",
        # " Lithuania Visa Application Center - Hyderabad ",
        " Lithuania Visa Application Center - Kolkata ",
        " Lithuania Visa Application Center - Mumbai "]

    if df["Appointment"][num].lower() == "delhi":
        listof = " Lithuania Visa Application Center - Delhi "
        
    elif df["Appointment"][num].lower() == "mumbai":
        listof = " Lithuania Visa Application Center - Mumbai "
        
    elif df["Appointment"][num].lower() == "bangalore":
        listof = " Lithuania Visa Application Center - Bangalore "
    
    elif df["Appointment"][num].lower() == "kolkata":
        listof = " Lithuania Visa Application Center - Kolkata "

    elif df["Appointment"][num].lower() == "hyderabad":
            listof = " Lithuania Visa Application Center - Hyderabad "

    elif df["Appointment"][num].lower() == "chennai":
        listof = " Lithuania Visa Application Center - Chennai ",    


    for e in listof:

        driver.find_element(By.XPATH,"//body").send_keys(Keys.PAGE_UP) 
        
        actions = ActionChains(driver)  
        print('[+] Checking ', )        
            
        time.sleep(3)
        #
        try:
            and1 = driver.find_element(By.XPATH,"//div[@class='mat-select-arrow ng-tns-c85-4']")
        except:
            and1 = driver.find_element(By.ID,"mat-select-0")

            

        and1.click()
        time.sleep(3)
        hello = driver.find_element(By.XPATH,f"//span[text()='{e}']/..")
        actions.move_to_element(hello).click().perform()

        time.sleep(13)
        val = " National Visa "
        #val = " Schengen Visa "
        sub = driver.find_element(By.XPATH,"//div[@class='mat-select-arrow-wrapper ng-tns-c87-8']")
        driver.execute_script("arguments[0].scrollIntoView();", sub)
        sub.click()
        hello = driver.find_element(By.XPATH,f"//span[text()='{val}']/..")
        
        actions.move_to_element(hello).click().perform()
        driver.execute_script("arguments[0].scrollIntoView();", and1)
        time.sleep(8)
        slot = driver.find_element(By.XPATH,"//div[@class='alert alert-info border-0 rounded-0']").text
        # print(slot)
        #
        try:
            slot = driver.find_element(By.XPATH,"//div[@class='alert alert-info border-0 rounded-0']").text
            if("Earliest Available Slot :" in slot):
                print('[+] Slot is Avaliable')

                time.sleep(5)

                butto=driver.find_element(By.XPATH,"(//button[@type='button'])[2]")
                driver.execute_script("arguments[0].scrollIntoView();", butto)
                time.sleep(1)
                butto.click()
                playsound(r'C:\Users\ABC\OneDrive\Documents\Python\ring.mp3')
                import smtplib

                sender_email = "dishamichi8@gmail.com"
                rec_email = "APPLYGOLDENWHALE@GMAIL.COM"
                password = "axxlxgxswdzimmfz"
                message = "Hey, this was sent using python.. Bot has get a slot and started booking now !"


                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.ehlo()
                    server.starttls()
                    server.ehlo()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, rec_email, message)
                    print('Sent to the Given gmail!')
                time.sleep(10)
                first = driver.find_element(By.ID,"mat-input-2")
                first.send_keys(fname)

                last = driver.find_element(By.ID,"mat-input-3")
                last.send_keys(lname)
                time.sleep(1)

                genders = df["Gender"][cnt].capitalize()
                genders = ' ' + genders + ' '
                print(genders)
                gender = driver.find_element(By.ID, "mat-select-value-7")
                driver.execute_script("arguments[0].scrollIntoView();", gender)
                gender.click()

                time.sleep(3)
                
                g=wait.until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{genders}']")))
                actions.move_to_element(g).click().perform()

                birth_ = driver.find_element(By.ID,"dateOfBirth")
                actions.move_to_element(birth_).click().perform()
                birth_.send_keys(birth_of)
                time.sleep(6)

                country = df["Country"][cnt]
                country = ' '+ country + ' '
                national = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='mat-select-arrow-wrapper ng-tns-c85-14']")))
                driver.execute_script("arguments[0].scrollIntoView();", national)
                national.click()
                time.sleep(3)
                hello = driver.find_element(By.XPATH,f"//span[text()='{country}']/..")
                actions = ActionChains(driver)
                actions.move_to_element(hello).click().perform()

                passport_holder = driver.find_element(By.ID,"mat-input-4")
                actions.move_to_element(passport_holder).click().perform()
                passport_holder.send_keys(passport)

                expiry = driver.find_element(By.ID,"passportExpirtyDate")
                actions.move_to_element(expiry).click().perform()
                expiry.send_keys(expirydate)
                time.sleep(4)
                codes = df["Code"][cnt]
                print(codes)
                time.sleep(2)
                try:
                    code_holder = driver.find_element(By.ID,"mat-input-5")
                    actions.move_to_element(code_holder).click().perform()
                    time.sleep(2)
                    code_holder.send_keys(codes)
                except:
                    try:
                        code_holder = driver.find_element(By.XPATH,"//*[@class='mat-form-field mat-form-field-outline-brand ng-tns-c59-16 mat-primary mat-form-field-type-mat-input mat-form-field-appearance-outline mat-form-field-can-float ng-pristine ng-invalid ng-star-inserted mat-form-field-invalid ng-touched']")
                        actions.move_to_element(code_holder).click().perform()
                        time.sleep(2)
                        code_holder.send_keys(codes)
                    except:pass
                try:
                    code_holder = driver.find_element(By.XPATH,"//*[@class='mat-form-field mat-form-field-outline-brand ng-tns-c59-16 mat-primary mat-form-field-type-mat-input mat-form-field-appearance-outline mat-form-field-can-float ng-pristine ng-invalid ng-star-inserted mat-form-field-invalid ng-touched']")
                    actions.move_to_element(code_holder).click().perform()
                    time.sleep(2)
                    code_holder.send_keys(codes)
                except:pass

                try:
                    code_holder.send_keys(codes)
                except:
                    try:
                        pyautogui.typewrite(codes)
                    except:pass
                # try:
                #     x, y = pyautogui.locateCenterOnScreen("ssk.png", confidence=0.8)
                #     pyautogui.moveTo(x, y)
                #     #time.sleep(10)
                #     #x, y = pyautogui.position()
                #     pyautogui.click(interval=1)
                #     pyautogui.typewrite(codes)
                #     time.sleep(2)
                #     # time.sleep(2)

                # except:pass

                time.sleep(2)
                phone_holder = driver.find_element(By.ID,"mat-input-6")
                actions.move_to_element(phone_holder).click().perform()
                phone_holder.send_keys(phonenumber)

                email_holder = driver.find_element(By.ID,"mat-input-7")
                actions.move_to_element(email_holder).click().perform()
                email_holder.send_keys(email_)

                
           
                time.sleep(7)
                driver.find_element(By.XPATH,"//*[text()=' Save ']/..").click()

                time.sleep(7)
                driver.find_element(By.XPATH,"//*[text()=' Continue ']/..").click()

                time.sleep(7)
                driver.find_element(By.XPATH,"//*[text()=' Generate OTP ']/..").click()

                link_="https://accounts.google.com/v3/signin/identifier?dsh=S-637052758%3A1666389744021673&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWo5xUf5kqvA2wZ4PM7VY76MS6UK1NV7idf5t_blXMDIlCU2bqYNTNTw_87WkHbPB_mLTY8I"

                driver.execute_script("window.open('https://accounts.google.com/v3/signin/identifier?dsh=S-905005946%3A1664808111575292&authuser=0&biz=false&cc=PK&continue=https%3A%2F%2Fmail.google.com&flowEntry=AddSession&flowName=GlifWebSignIn&hl=en&service=mail');")
                # Switch to the new window
                driver.switch_to.window(driver.window_handles[1])
                driver.get(link_)
                time.sleep(3)

                password_ = "@Waheguruji11"
                login_gmail(driver, wait, email, password_)

                driver.implicitly_wait(10)

                time.sleep(3)

                mail = driver.find_element(By.XPATH,"(//*[text()='donotreply'])[2]")
                driver.execute_script("arguments[0].scrollIntoView();", mail)
                mail.click()

                driver.implicitly_wait(10)
                time.sleep(5)

                code = driver.find_element(By.XPATH,"(//div[@class='adm']/../../p)[3]").text
                code = code.replace("The OTP for your application with VFS Global is", "")
                code = code.replace(". The OTP will expire in 3 mins.", "")
                code = code.replace(' ','')
                print(f'[+] Code is {code}')


                driver.switch_to.window(driver.window_handles[0])

                code_holder = driver.find_element(By.XPATH,"//input[@placeholder='OTP']")
                code_holder.send_keys(code)


                verify = driver.find_element(By.XPATH,"//*[text()=' Verify ']/..")
                verify.click()

                cnt += 1

                time.sleep(7)
                driver.find_element(By.XPATH,"//*[text()=' Continue ']/..").click()
                time.sleep(10)
                
                no = 1
                for b in range(42):
                    try:
                        h = driver.find_element(By.XPATH,f"(//div[@class='fc-daygrid-day-bottom']/../../..)[{no}]")
                        actions.move_to_element(h).click().perform()
                        no += 1
                    except:
                        h = driver.find_element(By.XPATH,f"(//div[@class='fc-daygrid-day-frame fc-scrollgrid-sync-inner'])[{no}]")
                        actions.move_to_element(h).click().perform()
                        no += 1
                    
                time.sleep(3)    
                times = driver.find_element(By.XPATH,"//input[@name='SlotRadio']")
                driver.execute_script("arguments[0].scrollIntoView();", times)
                times.click()
                time.sleep(2)

                c= driver.find_element(By.XPATH,"//*[text()=' Continue ']/..")
                actions.move_to_element(c).click().perform()
                time.sleep(5)

                xont = driver.find_element(By.XPATH,"//*[text()=' Continue ']/..")
                driver.execute_script("arguments[0].scrollIntoView();", xont)
                time.sleep(2)
                xont.click()
                time.sleep(8)

                try:
                    xont = driver.find_element(By.XPATH,"//*[text()=' Continue ']/..")
                    driver.execute_script("arguments[0].scrollIntoView();", xont)
                    time.sleep(2)
                    xont.click()
                except:pass

                time.sleep(8)

                try:
                    driver.find_element(By.XPATH,"(//span[@class='mat-checkbox-inner-container'])[1]//input").click()
                    time.sleep(2)
                except:pass

                try:
                    driver.find_element(By.XPATH,"(//span[@class='mat-checkbox-inner-container'])[1]").click()
                    time.sleep(2)
                except:pass

                try:
                    xont = driver.find_element(By.XPATH,"//*[text()=' Continue ']/..")
                    driver.execute_script("arguments[0].scrollIntoView();", xont)
                    time.sleep(2)
                    xont.click()
                except:pass

                time.sleep(18)

                print("[+] Done !")


                print('==========================================================')
                driver.quit()

            
            else:
                print('[+] Not slots Are Avalibale')
                
        except:
            pass            
         
        time.sleep(3)       

def login_gmail(driver, wait , email, passw): 
    
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, f"//input[@type='email']"))).send_keys(email)
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, f"//span[text()='Next']/.."))).click()
        time.sleep(12)
    except:
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, f"//span[text()='Next']/.."))).click()
        except:pass
                    
    time.sleep(4)
    wait.until(EC.presence_of_element_located((By.XPATH, f"//input[@type='password']"))).send_keys(passw)
    
    wait.until(EC.presence_of_element_located((By.XPATH, f"//span[text()='Next']/.."))).click()

    time.sleep(2)


def final_scraper():
    global wait
    
    wait = WebDriverWait(driver, 15)
    global email_
    global passw
    global  fname
    global lname
    global birth_of
    global passport, expirydate, codes, phonenumber, email
    try:
        email_ = df['Email'][cnt]
        email = "amanraman1821@gmail.com"
        passw = "@Waheguruji11"
        fname = df["fname"][cnt]
        lname = df["lname"][cnt]
        birth_of = str(df["Date of Birth"][cnt])
        birth_of = birth_of.replace('-', '/')
        birth_of = birth_of.replace('00:00:00','')
        birth_of = birth_of.split("/")
        birth_of.reverse()
        birth_of = str(birth_of)
        birth_of = birth_of.replace('[','')
        birth_of = birth_of.replace(']','')
        birth_of = birth_of.replace("'",'')
        birth_of = birth_of.replace(',','')
        birth_of = birth_of.replace(" ",'')
        global country
        country = " INDIA "
        expirydate = str(df["Passport Expiry"][cnt])
        expirydate = expirydate.replace('-', '/')
        expirydate = expirydate.replace('00:00:00','')
        expirydate = expirydate.split("/")
        expirydate.reverse()
        expirydate = str(expirydate)
        expirydate = expirydate.replace('[','')
        expirydate = expirydate.replace(']','')
        expirydate = expirydate.replace("'",'')
        expirydate = expirydate.replace(',','')
        expirydate = expirydate.replace(" ",'')
        passport = df["Passport no"][cnt]
        phonenumber = str(df["Number"][cnt])
    except:pass

    
    time.sleep(10)            
    try:
        login_username(email)
    except:
        time.sleep(6)
        login_username(email)

    login_password(passw)
    try:
        login()

        print('[+] Login Complete !')
        time.sleep(20)

        wait.until(EC.presence_of_element_located((By.XPATH, f"//button[@class='mat-focus-indicator btn mat-btn-lg btn-brand-orange d-none d-lg-inline-block position-absolute top-n3 right-0 z-index-999 mat-raised-button mat-button-base']"))).click()
        print('[+] Clicking on Booking Button ...')
        print('[+] Started Filling the Form')
        print('[+] It will automatically fill the form')
        time.sleep(7)
    except:pass
    

    
get_chrome()
print('[+] Opening Chrome !.......')
time.sleep(15)

final_scraper()

time.sleep(5)

try:
    x, y = pyautogui.locateCenterOnScreen("save.png", confidence=0.8)
    pyautogui.moveTo(x, y)
    #time.sleep(10)
    #x, y = pyautogui.position()
    pyautogui.click(interval=1)

    # time.sleep(2)

except:pass


time.sleep(3)
print('[+] Chceking For any Slot !..')

visa_application()


            
            

        