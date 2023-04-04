#!/usr/bin/env python
# coding: utf-8

# In[59]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import csv
from datetime import datetime
import time, datetime

with open('soscore_scraper.csv', 'w', newline='',encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Time", "Country", 'HomeTeam', "AwayTeam", "1", "X", "2", "HWR", "AWR", "HAWR","AAWR"])

from datetime import datetime
current = datetime.now()
current_date = f"{current.day}/{current.month}/{current.year}"
# print(current_date)
def get_chrome():
    global driver
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-infobars')

    url = 'https://www.sofascore.com/'
    print("Reqesting the website. Waiting for website response.....")
    driver = uc.Chrome(options=chrome_options)
    driver.get(url)
    print("Successfully Got the response.")

def scraper():
    # driver.refresh()
    time.sleep(2)
    list_of_countries = []
    driver.find_element(By.XPATH,"//input[@class='sc-a14b0fd8-1 iONBUB']").click()
    time.sleep(1.2)
    countries = driver.find_elements(By.XPATH,"//div[@class='sc-bqWxrE bHKFjr']")
    if len(countries) == 1:
    #     driver.refresh()
        time.sleep(6)
    print("Please wait so i can prepare for scraping.")
    for b in range(len(countries)):
        countries = driver.find_elements(By.XPATH,"//div[@class='sc-bqWxrE bHKFjr']")
        country = ""
        country = countries[b].text

        driver.find_element(By.XPATH,f"(//*[text()='{country}']/..)[1]").click()  
        time.sleep(5)
        c = 1
        times = driver.find_element(By.XPATH,"//span[@class='sc-bqWxrE gffDkV']").text
        matches = driver.find_elements(By.XPATH,"//div[@class='sc-hLBbgP dRtNhU sc-9199a964-1 kusmLq']/../../..")
        for x in range(len(matches)):
            one = driver.find_element(By.XPATH,f"(//span[@class='sc-bqWxrE dvoGHd'])[{c}]").text
            c += 1
            xx = driver.find_element(By.XPATH,f"(//span[@class='sc-bqWxrE dvoGHd'])[{c}]").text
            c += 1
            two = driver.find_element(By.XPATH,f"(//span[@class='sc-bqWxrE dvoGHd'])[{c}]").text
            
            try:
                match = matches[x]
                match.click()
                time.sleep(5)
            except:pass
            # driver.find_element(By.XPATH,"//*[text()='SHOW MORE']").click()
            # time.sleep(5)
            try:
                team1 = driver.find_element(By.XPATH,"(//span[@class='sc-bqWxrE bmDGoJ'])[1]").text
                team2 = driver.find_element(By.XPATH,"(//span[@class='sc-bqWxrE bmDGoJ'])[2]").text
                print(f"{team1} Versus {team2}")
            except:pass
#             try:
#                 driver.find_element(By.XPATH,"//div[@class='sc-hLBbgP kQrZrw']").click()
#             except:pass
            time.sleep(1)
            full_time_team1 = ""
            full_time_team2 = ""
            full_time_draw = ""
            double_chance_team1 = ""
            double_chance_team2 = ""
            double_chance_draw = ""
            both_score_yes = ""
            both_score_no = ""
            try:
                full_time_team1 = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[1]").text
            except:pass
            try:
                full_time_team2 = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[3]").text
            except:pass
            try:
                full_time_draw = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[2]").text
            except:pass
            try:
                double_chance_team1 = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[4]").text
            except:pass
            try:
                double_chance_team2 = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[6]").text
            except:pass
            try:
                double_chance_draw = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[5]").text
            except:pass
            try:
                both_score_yes = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[12]").text
            except:pass
            try:
                both_score_no = driver.find_element(By.XPATH,"(//a[@class='sc-hLBbgP sc-eDvSVe fXULfy ktIiSI']//div//span)[13]").text
            except:pass

            try:
                team1_odds = driver.find_element(By.XPATH,"(//span[@class='sc-bqWxrE kjYNia'])[1]").text
            except:
                team1_odds = ''
            try:
                team2_odds = driver.find_element(By.XPATH,"(//span[@class='sc-bqWxrE kjYNia'])[2]").text
            except:
                team2_odds = ''
            try:
                refree_name = driver.find_element(By.XPATH,"//div[@class='sc-hLBbgP sc-eDvSVe jgZvpA fRddxb']//span[@class='sc-bqWxrE eiDbGU']").text
            except:
                refree_name = ''
            try:
                location = driver.find_element(By.XPATH,"//div[@class='sc-hLBbgP sc-eDvSVe gjJmZQ fRddxb']//span[@class='sc-bqWxrE exWvDt']").text
            except:
                location = ""

        #     x += 1
            print(x)
            time.sleep(0.2)
            #coun1 = "Englan/d"
            with open('soscore_scraper.csv', 'a', newline='',encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([current_date, times, country, team1, team2, one, xx, two, full_time_team1, full_time_team2, full_time_draw, double_chance_team1, double_chance_team2, double_chance_draw, both_score_yes, both_score_no])
                    print("Written into csv file.")
            print("-----------------------------------------------------------------------------------------------------")

        driver.back()
        time.sleep(3)
        time.sleep(1)
def main():
    print("Welcome, I am bot and you can run me as ever you want.")
    get_chrome()
    scraper()
    print("Good Bye!")
    driver.quit()
        
if __name__ in "__main__":
    main()


# 
