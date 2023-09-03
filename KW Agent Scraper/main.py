from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
import time
import os


print("[+] Hey, Please make sure that your all zips code should be contain in 'azip.txt'.")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
# ChromeDriverManager().install(),
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://console.command.kw.com/command/referrals/grow-my-network')
time.sleep(2)
wait = WebDriverWait(driver, 15)
username = "<your username>"
password = "<your password>"
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-id='signIn']"))).click()
driver.implicitly_wait(6)
zip_list = []
print("[+] Reading your txt file.")
with open("azip.txt", "r") as file:
    lines = file.readlines()
    zip_list.extend([line.strip() for line in lines])

if os.path.exists('output.csv') == False:
    with open('output.csv', 'a', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Zip Code", "Agent Full Name", "Team Leader Status", "Agent Team Name", "Office Phone Number", "Personal Phone Number", "Email",
                "Closed Units In Area", "Closed Units", "Listing Sold", "Buy Sides", "Leases",
                "Sales Volume / 12 mins", "Average Deal Size"])
for zip in zip_list:
    time.sleep(1)
    print("[+] Zip Code is : ", zip)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search map']"))).clear()
    wait2 = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search map']"))).send_keys(zip)
    time.sleep(0.5)
    locations = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='pac-container pac-logo hdpi']//div[@class='pac-item']")))
    try:
        loc = ""
        location_text = ""
        for location in locations:
            location2 = str(location.text)
            if "USA" in location2:
                location_text = location2
                loc = location
                break

        loc.click()
        if "USA" in location_text:
            # wait2.until(EC.presence_of_element_located((By.XPATH,"(//div[@class='pac-container pac-logo hdpi']//div[@class='pac-item'])[1]"))).click()
            time.sleep(7)
        
            try:
                agents_list = list(wait.until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[@class='d-flex flex-column py-3 pr-3 pl-2']"))))
                # print(agents_list)
                total_results = int(driver.find_element(By.XPATH, "//div[text()='Results']//div").text)
                print("[+] Total Agents Found : ", total_results)
                agent_no = 0
                for agent_no2 in range(total_results):
                    agent_no += 1
                    
                    try:
                        driver.find_element(By.XPATH, f"//span[@aria-label='close accordion']").click()
                        time.sleep(0.76)
                    except:
                        pass
                    try:
                        driver.find_element(By.XPATH, f"(//span[@aria-label='open accordion'])[{agent_no}]").click()
                    except:
                        pass
                    time.sleep(1)

                    full_name = wait.until(EC.presence_of_element_located((By.XPATH,
                                                    f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']//h4)[{agent_no}]"))).text
                    try:
                        office_phone = driver.find_element(By.XPATH,
                                                f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Phone']/..//p[2])[{agent_no}]").text
                    except:office_phone = ''

                    try:
                        email = driver.find_element(By.XPATH,
                                                    f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Email']/..//a)[{agent_no}]").text
                    except:email = ''

                    try:
                        closed_unit_in_area = driver.find_element(By.XPATH,
                                                                f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Closed Units in this Area']/..//p[2])[{agent_no}]").text
                    except:closed_unit_in_area = ''

                    try:
                        closed_units = driver.find_element(By.XPATH,f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Closed Units']/..//p[2])[{agent_no}]").text
                    except:closed_units = ''

                    try:
                        listings_sold = driver.find_element(By.XPATH, f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Listings Sold']/..//p[2])[{agent_no}]").text
                    except:listings_sold = ''

                    try:
                        buy_sides = driver.find_element(By.XPATH,
                                                        f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Buy Sides']/..//p[2])[{agent_no}]").text
                    except:buy_sides = ''

                    try:
                        leases = driver.find_element(By.XPATH,
                                                    f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Leases']/..//p[2])[{agent_no}]").text
                    except:leases = ''

                    try:
                        sales_volume_12_mins = driver.find_element(By.XPATH,
                                                                f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Sales volume / last 12m']/..//p[2])[{agent_no}]").text
                    except:sales_volume_12_mins = ''

                    try:
                        average_deal_size = driver.find_element(By.XPATH,
                                                                f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Average deal size']/..//p[2])[{agent_no}]").text
                    except:average_deal_size = ''

                    action_chains = ActionChains(driver)
                    if len(agents_list)-1 == agent_no:
                        print("[+] Loading More Profiles ")
                        element = driver.find_element(By.XPATH, f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']/..//*[text()='Average deal size']/..//p[2])[{agent_no}]")
                        action_chains.move_to_element(element).perform()
                        time.sleep(1)
                        
                    try:
                        team = driver.find_element(By.XPATH,
                                                f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2'])[{agent_no}]/..//*[text()='Team']/..//ul/li/p").text
                    except Exception as ex:
                        # print(ex)
                        team = ''

                    agent_link = str(driver.find_element(By.XPATH,
                                                        f"(//div[@class='d-flex flex-column py-3 pr-3 pl-2']//h4/..)[{agent_no}]").get_attribute('href'))
                    print("[+] Agent Link ", agent_link)
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(agent_link)
                    time.sleep(3)
                    team_leader = ""
                    if team != "":
                        try:
                            team_leader_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Team Leader (Rainmaker)']")))
                            team_leader = 'Yes'
                        except Exception:
                            team_leader = 'No'

                    try:
                        private_phone_number = driver.find_element(By.XPATH,"//*[text()='Primary Phone']/..")
                        private_phone_number = str(private_phone_number.get_attribute('innerHTML')).split('</div>')[1]
                    except Exception as ex:
                        print(ex)
                        private_phone_number = ''
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                    with open('output.csv', 'a', newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow([zip, full_name, team_leader, team, office_phone, private_phone_number, email, closed_unit_in_area, closed_units,
                                        listings_sold, buy_sides, leases, sales_volume_12_mins, average_deal_size])
            except Exception as ex:
                with open('output.csv', 'a', newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow([zip, "No Agents Found."])
                print("[+] No agents found! ")
                print("Error : ", ex)
                pass

    except Exception as ex:
        print("[+] Error :  ", ex)
        print("[+] No such type of Zip Code found!")
        with open('output.csv', 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([zip, "No such type of Zip Code found!"])
        pass

