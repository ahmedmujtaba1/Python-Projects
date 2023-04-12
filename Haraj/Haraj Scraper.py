#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
except:
    print("Any Module is not download")


# In[2]:


chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')

url = 'https://haraj.com.sa/'

driver = uc.Chrome(options=chrome_options)
driver.get(url)


# In[3]:


with open('Haraj_com_sa.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Category','Sub-Category','Type','Title',"City","numbers of time mentioned","Url"])


# In[ ]:


category_list = driver.find_elements(By.XPATH,"//li[@data-testid='main_tab']")
def next_step():
    try: 
        sub_cae_list = driver.find_elements(By.XPATH,"//ul[@data-testid='ul_tags_1']//li//h2//a")
        xn = 0
        for x in range(len(sub_cate_list)):
            xn += 1

    #             sub_cate_list = driver.find_elements(By.XPATH,"//ul[@data-testid='ul_tags_1']//li//h2//a")
            sub_category = sub_cate_list[x]
            sub_category_text = driver.find_element(By.XPATH,f"(//ul[@data-testid='ul_tags_1']//li//h2//a)[{xn}]").text
            print("Sub-Category: ",sub_category_text)
            sub_category.click()
            time.sleep(4)
            type_list = driver.find_elements(By.XPATH,"//ul[@data-testid='ul_tags_2']//li//h2//a")
            bbn = -1
            for bb in range(len(type_list)):
                try:
                    bbn += 1
                    try:
                        type_list = driver.find_elements(By.XPATH,"//ul[@data-testid='ul_tags_2']//li//h2//a")
                        type_text = type_list[bb].text
                    except:
                        type_list = driver.find_elements(By.XPATH,"//ul[@data-testid='ul_tags_2']//li//a")
                        type_text = type_list[bb].text
                    print("Type: ", type_text)
                    type_cate = type_list[bb]
                    type_cate.click()
                    time.sleep(6)
                except:
                    type_text = "No type found!"
                products = driver.find_elements(By.XPATH,"//h2")
                print("There are products found untill now: ", len(products))
                cnt = 1
                nn = 0
                for n in range(len(products)):
                    nn += 1
                    try:
                        driver.find_element(By.XPATH,"//button[@data-testid='posts-load-more']").click()
                        time.sleep(4)
                        print("Has clicked on 'Load More' button")
                    except:pass
                    products = driver.find_elements(By.XPATH,"//h2")
                    title = products[n].text
                    print("Title: ", title)
                    url = driver.find_element(By.XPATH,f"(//h2/..)[{nn}]").get_attribute("href")
                    goi = products[n]
                    goi.click()
                    time.sleep(5.3)
                    location = driver.find_element(By.XPATH,f"(//div[@class='flex items-center gap-2 text-sm']//span//a//span)[{cnt}]").text
                    print("Location: ", location)
                    include = 0
                    search_terms = ["اقسات", "term2", "term3"]
                    try:
                        replies = driver.find_elements(By.XPATH,"//p[@class='block max-w-full overflow-hidden break-words']")
                        
                        for term in search_terms:
                            try:
                                replies = driver.find_elements(By.XPATH,"//p[@class='block max-w-full overflow-hidden break-words']")

                                for txt in replies:
                                    if term in txt:
                                        include += 1
                            except:
                                pass
                    except:pass
                    print("Number of time mentioned: ", include)
                    driver.back()
                    time.sleep(4)
                    with open('Haraj_com_sa.csv', 'a', newline='', encoding='utf-8-sig') as file:
                        writer = csv.writer(file)
                        writer.writerow([category_text, sub_category_text, type_text, title, location, include, url])
                        print("Writen in csv file")
                        print("--------------------------------------------------------------------")
    except Exception as ex:
        print(ex)
        driver.get("https://haraj.com.sa/")
        time.sleep(5)
#         break
        
inn = 1
for i in range(len(category_list)):
    category_list = driver.find_elements(By.XPATH,"//li[@data-testid='main_tab']")
    category = driver.find_element(By.XPATH,f"(//li[@data-testid='main_tab']//a//span)[{inn}]")
    category.click()
    time.sleep(7)
    category_text = driver.find_element(By.XPATH,f"(//li[@data-testid='main_tab']//a)[{inn}]").text
    print("Main-Category: ",category_text)
    time.sleep(0.4)
    sub_cate_list = driver.find_elements(By.XPATH,"//ul[@data-testid='ul_tags_1']//li//h2//a")
    next_step()
    inn += 1


# In[ ]:




