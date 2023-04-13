import undetected_chromedriver as uc
import time
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import random

# with open('etsy_scraper.csv', 'w', newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Business Name","Store Link","Sales","Seller First Name","Seller Last Name","Email","Facebook Page","Instagram Page"])

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

url = input("Input Your category Link: ")
driver = uc.Chrome(options=chrome_options)
driver.get(url)#enter you url
time.sleep(10)


driver.switch_to.window(driver.window_handles[0])
cnt = int(input("How many data do you want?: "))
list_of_sellers = ["djk"]
page_number = 1
good_leads = 0
totalcount = 0
leadsPerpage = 0
actions = ActionChains(driver)
while good_leads != cnt:
    if page_number != 1:
        url1 = f"{url}&page={page_number}"
        driver.get(url1)
    time.sleep(7)
    leadsPerpage = 1
    page_number += 1
    try:
        listd = driver.find_elements(By.XPATH,"//*[text()='Star Seller']/../../..")#only will scrape "star seller"
            
        for i in range(len(listd)):
            if(totalcount==cnt):
                break
            
            email_ = ''
            facebook = ""
            instagram = ""
            first_name = ""
            last_name = ""
            websiteOr = ""
            result= listd[i]
            result.click()
            # time.sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(7)
            try:
                shop_name = driver.find_element(By.XPATH,"(//a[@class='wt-text-link-no-underline'])[8]//span").text
            except:
                shop_name = driver.find_element(By.XPATH,"//a[@class='wt-text-link-no-underline wt-text-black']").text

            leadsPerpage += 1
#                 print("KSJ", leadsPerpage)
            for ka in range(len(list_of_sellers)):
                re = "No"
                if(shop_name in list_of_sellers[ka]):
                    re = "Yes"
                    break

            if "No" in re:

                list_of_sellers.append(shop_name)
                totalcount +=1

                try:
                    print("Shop Name : ", shop_name)
                    try:
                        sales = driver.find_element(By.XPATH,"//span[@class='wt-text-caption ']").text
                        isi = sales.replace('sales','')
                        isi = isi.replace(' ','')
                        isi = isi.replace(',','')
                        isi = int(isi)
                    except:
                        sales = "Not provided"
                        isi = 0
#                         print("Sales : ",sales)

                    if isi >= 300 or sales == "Not provided":
                        try:
                            shop_name_link= driver.find_element(By.XPATH,"//a[@class='wt-text-link-no-underline wt-text-black']").get_attribute('href')   
                        except:
                            time.sleep(4)
                            try:
                                shop_name_link= driver.find_element(By.XPATH,"(//a[@class='wt-text-link-no-underline'])[8]").get_attribute('href')
                            except:
                                shop_name_link = ""
                        print("Shop Link : ", shop_name_link)

                        from bs4 import BeautifulSoup 
                        import requests

                        r = requests.get(shop_name_link)
                        time.sleep(2)
                        if sales == "Not provided":
                            soup = BeautifulSoup(r.content, 'html.parser')
                            sales = soup.find('span', attrs = {"class":"wt-text-caption wt-no-wrap"}).text
                        print("Sales : ",sales)

                        try:
                            soup = BeautifulSoup(r.content, 'html.parser')
                            table = soup.find_all('div', attrs = {'class' : 'img-container'})[1]
                            # print(table)
                            seller_name = table.find('p')
                            seller_name = seller_name.text
                            seller_name_list = seller_name.split(" ")
                            first_name = seller_name_list[0]
                            try:
                                last_name = seller_name_list[1]
                                print("Seller Full Name: ", first_name, last_name)
                            except:
                                print("Seller Full Name: ", first_name)
                        except:
                            try:
                                soup = BeautifulSoup(r.content, 'html.parser')
                                table = soup.find_all('div', attrs = {'class' : 'img-container'})[0]
                                # print(table)
                                seller_name = table.find('p')
                                seller_name=seller_name.text
                                seller_name_list = seller_name.split(" ")
                                first_name = seller_name_list[0]
                                try:
                                    last_name = seller_name_list[1]
                                    print("Seller Full Name: ", first_name, last_name)
                                except:
                                    print("Seller Full Name: ", first_name)
                            except Exception as ex:
                                    print(ex)


                        driver.get(shop_name_link)
                        time.sleep(10)                   
                        try:
                            instagram = driver.find_element(By.XPATH,"//a[@aria-label='Instagram']").get_attribute('href')

                        except:
                            print("There is no instagram!")
                            pass

                        try:
                            facebook = driver.find_element(By.XPATH,"//a[@aria-label='Facebook']").get_attribute('href')
                            driver.get(facebook)
                            time.sleep(6)

                            try:
                                driver.find_element(By.ID,"email").send_keys("chistinanadia458@gmail.com")
                                time.sleep(0.34)
                                driver.find_element(By.ID,"pass").send_keys("myhappyfamily12")
                                driver.find_element(By.XPATH,"//*[text()='Log in']").click()
                                time.sleep(7)

                            except:pass     
                            FacebookText = driver.find_elements(By.XPATH,"//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1nhvcw1 x1qjc9v5 xozqiw3 x1q0g3np xyamay9 xykv574 xbmpl8g x4cne27 xifccgj']//div//div//span")
                            websiteOr = "No"
                            for m in FacebookText:
                                m = m.text
                            #     print(m)
                                if "@" in m:
                                    email_ = m
                                    print(email_)


                                if "www." in m or "Www." in m or ".com" in m or ".co" in m or ".uk" in m or ".ca" in m:
                                    website = m
                                    if "etsy" in website:
                                        websiteOr = "Yes"
                                        break
                            time.sleep(5)

                        except:
                            print("There is no Facebook!")
                            pass     

                        if email_ == "":

                            number = [1,2]
                            no = random.choice(number)
                            if no == 1:
                                email_ = shop_name.lower() + "@gmail.com"
                            elif no == 2:
                                email_ = seller_name.lower() + "@yahoo.com"
                            print("Fake Generated email", email_)
                        if websiteOr == "Yes":

                            if facebook == "": 
                                pass
                            elif instagram == "":
                                pass
                            else:

                                good_leads += 1
                                with open('etsy_scraper.csv', 'a', newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([shop_name, shop_name_link, sales, first_name, last_name, email_, facebook, instagram, url])
                                    print("Written in csv file")
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        print(totalcount)
                        print('----------------------------------------------------------------------')
                        print("Good Leads are found till now. ", good_leads)
                        print('----------------------------------------------------------------------')
                    else:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        time.sleep(5)                                               

                except:pass



            elif "Yes" in re:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(5)
            
    except:
        try:
            try:
                page_number = driver.find_element(By.XPATH,"(//a[@class='wt-btn wt-btn--filled wt-action-group__item wt-btn--small wt-btn--icon'])[4]").click()
            except:
                page_number = driver.find_element(By.XPATH,"(//a[@class='wt-btn wt-btn--filled wt-action-group__item wt-btn--small wt-btn--icon'])[2]").click()
            actions.move_to_element(page_number).click().perform()
            time.sleep(7)
            page_number +=1
            print("Page Number is : ", page_number)
        except:pass