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
    from getpass import getpass
    import pwinput
except:
    print("Any Module is not download")

print("Hey, I am bot and I will ask some question to proceed to final stage................Let's Go")
login_username = input("Enter your Facebook Username OR email?: ")
# login_password = getpass("Enter your Facebook Password? (PASSWORD WILL NOT SEE): ")
login_password = pwinput.pwinput(prompt='Enter your Facebook Password?: ', mask='*')
share_url = input("Enter your Share URL: ")
message = input("Type your message! : ")
type_ = input("What is your default audience for this post. [Public,Friends?]: ")
if type_ == "Public" or type_ == "public":
    type_ = "Public"
elif type_ == "Friends" or type_ == "friends":
    type_ = "Friends"

def pub(username,passw,share_url):
    global driver
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block 
        "profile.default_content_setting_values.media_stream_camera": 1,  # 1:allow, 2:block 
        "profile.default_content_setting_values.geolocation": 1,          # 1:allow, 2:block 
        "profile.default_content_setting_values.notifications": 1         # 1:allow, 2:block 
     })
    
    url = 'https://www.facebook.com/login/'
    driver = uc.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(8)
    try:
        driver.find_element(By.ID,"email").clear()
        time.sleep(0.7)
        driver.find_element(By.ID,"email").send_keys(login_username)
        time.sleep(0.3)
        driver.find_element(By.ID,"pass").send_keys(login_password)
        driver.find_element(By.XPATH,"//*[text()='Log in']").click()
        time.sleep(9)
    except:
        while True:
            driver.find_element(By.ID,"pass").send_keys(passw)
            driver.find_element(By.XPATH,"//*[text()='Log in']").click()
            time.sleep(9)


            try:
                driver.find_element(By.XPATH,"//a[@href='https://www.facebook.com/recover/initiate?lwv=120&lwc=1348092&ars=facebook_login_pw_error']")
                print("Password is wrong")
                passw = pwinput.pwinput(prompt='Enter your Facebook Password?: ', mask='*') 
            except:
                print("Successfully logged in")
                break
    try:
        driver.find_element(By.XPATH,"//input[@value='Not Now']").click()
    except:pass
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[@class='x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x78zum5 x1egjynq x1ou2tus x1yrsyyn x10b6aqq']").click()
    time.sleep(5)
   
    driver.find_element(By.XPATH,"(//a[@class='x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou xe8uvvx xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz xjyslct xjbqb8w x18o3ruo x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1heor9g x1ypdohk xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1vjfegm x3nfvp2 xrbpyxo xng8ra x16dsc37'])[3]").click()
    time.sleep(6)
    friendList2 = []
    friendsList = driver.find_elements(By.XPATH,"//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u']")

    for friend in friendsList:
        try:
            friend = friend.text
            if friend == "":
                pass
            else:
                friendList2.append(friend)
        except Exception as ex:
            print(ex)

    print(f"There are {len(friendList2)} friends")
    driver.get("https://www.facebook.com/")
    time.sleep(5)

def amigos():
    
    driver.find_element(By.XPATH,"//div[@class='x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe xi81zsa']").click()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH,"//div[@aria-label='Done']").click()
        time.sleep(5)
    except:pass
    driver.find_element(By.XPATH,"//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']").send_keys(message)
    time.sleep(0.6)
    driver.find_element(By.XPATH,"//div[@aria-label='Post']")
    time.sleep(5)
    print("Successfully POSTED!")
    
    
pub(login_username, login_password, share_url)
while True:
    amigos()
    m = input("Do you want to proceed more?: [y OR n]")
    if m == "y":
        message = input("Type your message! : ")
        type_ = input("What is your default audience for this post. [Public,Friends?]: ")
        if type_ == "Public" or type_ == "public":
            type_ = "Public"
        elif type_ == "Friends" or type_ == "friends":
            type_ = "Friends"
        amigos()
        time.sleep(1)
        
    elif m == "n":
        break