try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    import undetected_chromedriver as uc
    from bs4 import BeautifulSoup
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.header import Header
    import csv, time, requests, re, smtplib, datetime
except:
    print("Any Module is not download")

with open('data.csv', 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Resturant Name", "Website", "Email", "Phone Number", "Instagram", "Facebook"])
driver = uc.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/search?client=opera-gx&hs=Kiu&sca_esv=556729110&tbs=lf:1,lf_ui:9&tbm=lcl&sxsrf=AB5stBiKFtZk1JZAX2F7E75NJPaurxXVfA:1692012619208&q=all+restaurant+in+usa&rflfq=1&num=10&sa=X&ved=2ahUKEwiP8f2YhtyAAxXhg_0HHRzkBr0QjGp6BAhaEAE&biw=1239&bih=579&dpr=1.5#rlfi=hd:;si:;mv:[[42.6318315,-68.8242032],[29.2240052,-121.17424489999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u5!2m2!5m1!1sgcid_3american_1restaurant!1m4!1u5!2m2!5m1!1sgcid_3seafood_1restaurant!1m4!1u2!2m2!2m1!1e1!1m4!1u1!2m2!1m1!1e1!1m4!1u1!2m2!1m1!1e2!1m4!1u22!2m2!21m1!1e1!2m1!1e2!2m1!1e5!2m1!1e1!2m1!1e3!3sIAEqAlVT,lf:1,lf_ui:9")
time.sleep(8)
wait = WebDriverWait(driver, 15)
card_container = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='vwVdIc wzN8Ac rllt__link a-no-hover-decoration']")))
cnt = 0
cnt2 = 0
for i in range(1000):
    try:
        cnt += 1
        cnt2 += 1
        resturant_name = driver.find_element(By.XPATH, f"(//a[@class='vwVdIc wzN8Ac rllt__link a-no-hover-decoration']//div[@class='rllt__details']//div[@role='heading']//span)[{cnt}]").text
        card = card_container[cnt2].click()
        time.sleep(3)
        try:
            website = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Website']/../.."))).get_attribute('href')
        except:
            website = ""
        try:
            phone_number = driver.find_element(By.XPATH,"//*[text()='Phone']/../..//span[2]//a//span").text
        except:
            phone_number = ""
        try:
            instagram = driver.find_element(By.XPATH,"//*[text()='Instagram']/..").get_attribute('href')
        except:
            instagram = ""
        try:
            facebook = driver.find_element(By.XPATH,"//*[text()='Facebook']/..").get_attribute('href')
        except:
            facebook = ""
        
        url = f"{website}"
        headers = {
            "Authority" : f"{website}",
            "Method" : "GET",
            "Path" : "/",
            "Scheme" : "https",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding" : "gzip, deflate, br",
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0",
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            content = response.text
            
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            emails_found = re.findall(email_pattern, content)
            
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        

    
        print("Website : ", website)
        print("All Email Found : ", emails_found)
        # print("Email : ", email)
        print("Resturant Name : ", resturant_name)
        print("Phone Number : ", phone_number)
        print("Instagram : ", instagram)
        print("Facebook : ", facebook)

        sent_emails = list()

        for email in emails_found:
            if email not in sent_emails:
                if str(email) != "user@domain.com":
                    sent_emails.append(email)
                    sender_email = "your email"
                    rec_email = str(email)
                    password = "your app password"
                    subject = "Grow Your Bussiness With US"

                    message = MIMEMultipart("alternative")
                    message["From"] = sender_email
                    message["To"] = rec_email
                    message["Subject"] = Header(subject, "utf-8")

                    html_content = f"""
                    <html>
                    <head>
                        <style>
                            .container {{
                                width: 80%;
                                margin: auto;
                                padding: 20px;
                                border: 1px solid #ccc;
                                background-color: #f7f7f7;
                                font-family: Arial, sans-serif;
                            }}
                            .header {{
                                background-color: #007bff;
                                color: #fff;
                                padding: 10px;
                                text-align: center;
                                font-size: 20px;
                            }}
                            .signature {{
                                margin-top: 20px;
                                font-weight: bold;
                            }}
                            .link {{
                                color: #007bff;
                                text-decoration: none;
                            }}
                            .profile-button {{
                                display: inline-block;
                                padding: 10px 20px;
                                background-color: #007bff;
                                color: #fff;
                                border: none;
                                border-radius: 5px;
                                text-decoration: none;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="header">
                            {"SAM TECH"}
                        </div>
                        <div class="container">
                            <p><strong>Dear {resturant_name},<strong/></p>
                            <p>Date : {datetime.datetime.now()},</p>
                            <p>Subject : Grow Your Bussiness With Us</p>
                            
                            <p>In the changing world of food delivery, using web scraping is important for restaurants to succeed. The online food delivery market is expected to grow a lot, reaching $147 billion by the end of 2023 and $192 billion by 2025. Web scraping helps restaurants get important information from other places, like what competitors are doing, how to set prices, and how to advertise better. By using this scraped data, you can learn about new trends, make your food better, and stay in the game.</p>
                            <p>When you look at what other restaurants are offering, their prices, and what customers say, you can improve your own menu and prices. It's important to do web scraping in a fair and private way. This can give you a lot of good information to make smart choices and help your food delivery business do well.</p>
                            <p>If you want a special solution, {"SAM TECH"} can help with custom tools that give you real-time data to make your restaurant even better. You can find out more on <a class="link" href="https://rb.gy/1nr3g">Fiverr</a> and take your food delivery business to the next level.</p>
                            <p class="signature">Best regards,<br>{"Saad Mohsin, CEO of SAM TECH"}</p>
                            <p class="signature">Phone Number : <a href='https://api.whatsapp.com/send/?phone=923312269636&text&type=phone_number&app_absent=0'>+92 331 2269636</a></p>
                        </div>
                        <div style="text-align: center; margin-top: 20px; color: #fff;">
                            <a class="profile-button" href="https://www.github.com/ahmedmujtaba1">Visit My Profile</a>
                        </div>
                    </body>
                    </html>
                    """

                    html_part = MIMEText(html_content, "html")
                    message.attach(html_part)

                    try:
                        with smtplib.SMTP('smtp.gmail.com', 587) as server:
                            server.ehlo()
                            server.starttls()
                            server.ehlo()
                            server.login(sender_email, password)
                            server.sendmail(sender_email, rec_email, message.as_string())
                        print('Email sent successfully to ', email, "!")
                    except Exception as e:
                        print(f'An error occurred: {e}')

        with open('data.csv', 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([resturant_name, website, emails_found, phone_number, instagram, facebook])
        print("--------------------------------------")
    except:
        next_page_url = driver.find_element(By.XPATH,"(//span[text()='Next']/..)[1]").get_attribute('href')
        driver.get(next_page_url)
        time.sleep(8)
        wait = WebDriverWait(driver, 15)
        card_container = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[@class='vwVdIc wzN8Ac rllt__link a-no-hover-decoration']")))
        cnt = 0
        cnt2 = 0
