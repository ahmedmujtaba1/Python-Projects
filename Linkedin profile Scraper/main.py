import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
# from solveRecaptcha import solveRecaptcha
import time, csv, customtkinter, re, pycountry

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("dark-blue") 


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("Email Extractor")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_left.grid_rowconfigure(0, minsize=10)  
        self.frame_left.grid_rowconfigure(5, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)    
        self.frame_left.grid_rowconfigure(11, minsize=10) 

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Email Extractor",
                                              )  
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.start_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Start",
                                                fg_color=("green", "green"),
                                                command=self.GetProfiles)
        self.start_button.grid(row=2, column=0, pady=10, padx=20)

        self.stop_button = customtkinter.CTkButton(master=self.frame_left,
                                                text="Stop",
                                                fg_color=("red", "red"),  
                                                command=self.stop_program)
        self.stop_button.grid(row=3, column=0, pady=10, padx=20)

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.keywords = customtkinter.CTkTextbox(master=self.frame_right,
                                            width=120,
                                            height=90
                                            )
        self.keywords.insert("0.0", "Keywords")
        self.keywords.grid(row=1, column=0, columnspan=1, pady=10, padx=5, sticky="we")
        self.leads_no = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="How many leads to scrape?")
        self.leads_no.grid(row=2, column=0, columnspan=1, pady=10, padx=5, sticky="we")
        location = customtkinter.StringVar(value="Location")
        world_countries = list(pycountry.countries)
        country_names = [country.name for country in world_countries]

        self.locations = customtkinter.CTkOptionMenu(master=self.frame_right,values=country_names,
                                         variable=location)
        self.locations.grid(row=3, column=0, columnspan=1, pady=10, padx=5, sticky="we")

        self.switch_2.select()
    
    def stop_program(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

    def GetProfiles(self):
        try:
            self.chrome_options = uc.ChromeOptions()
            self.chrome_options.add_argument("--disable-notifications")
            self.chrome_options.add_argument("--disable-popup-blocking")
            path = r"B:\Ahmed'sCode\Fiverr\Linkedin-Scraper-master\Solver"
            self.chrome_options.add_argument("--start-maximized")
            self.chrome_options.add_argument(f'--load-extension={path}')
            self.driver = uc.Chrome(options=self.chrome_options)
            self.driver.maximize_window()
            self.driver.get('chrome-extension://dgnocnoicfjbocfdmjigdhfjhinhpmcc/index.html')
            time.sleep(2.2)
            try:
                self.driver.find_element(By.ID,"edit").click()
            except:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH,"//div[@id='edit']/../input"))).send_keys(<your api key>)
            time.sleep(0.8)
            WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH,"//div[@id='edit']/../input"))).send_keys(<your api key>)
            self.driver.find_element(By.ID,"plan").click()
            time.sleep(2.3)

            try:
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.XPATH,"//option[@value='FREE']"))).click()
            except:
                time.sleep(2)
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH,"//div[@id='edit']/../input")))

            time.sleep(2)
            self.driver.find_element(By.ID,"rcdiv").click()
            time.sleep(0.3)
            self.driver.find_element(By.ID,"RclickDelay").clear()
            self.driver.find_element(By.ID,"RclickDelay").send_keys(10)
            self.driver.find_element(By.ID,"hcdiv").click()
            time.sleep(0.3)
            self.driver.find_element(By.ID,"hCap").click()
            self.keywords = self.keywords.get("1.0",'end-1c')
            print("Keywords : ", self.keywords)
            self.page = self.leads_no.get()
            self.location = self.locations.get()

            self.keywords = str(self.keywords).split(',')
            for self.keyword in self.keywords:
                profiles = []
                self.keyword = self.keyword.replace("\t","")
                self.keyword = self.keyword.replace("\n","")
                csv_filename = f'output/linkedin_result-{self.keyword}.csv'
                with open(csv_filename, mode='w', newline='', encoding="utf-8") as csv_file:
                    fieldnames = ['linkedin_url', 'email']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()

                total_leads = 0
                total_leads1 = 1
                while total_leads <= int(self.page):
                    wait = WebDriverWait(self.driver, 10)
                    email_types = [
                        "yahoo.com",
                        "aol.com",
                        "mail.com",
                        "gmx.com",
                        "hotmail.com",
                    ]
                    profile_no = 0
                    email_count = 0
                    tab_no = 0
                    if total_leads == int(self.page):
                        break
                    for email_type in email_types:
                        flag = True
                        hh = True
                        
                        if hh:
                            self.driver.get(f'https://www.google.com/search?q=%22{self.keyword.replace(" ","+")}%22email%3A+%22%40{email_type}%22+site%3Awww.linkedin.com%2Fin%2F+OR+site%3Awww.linkedin.com%2Fpub%2F%221..1000&sca_esv=566068857&cs=0&filter=0&biw=1280&bih=558&dpr=1.5#ip=1')
                            
                            if total_leads == int(self.page):
                                break
                            while flag:
                                # print("TOTAL LEAD : ", self.page)
                                if hh == False:
                                    tab_no += 1
                                    profile_no  = 0
                                    print("Moving to this email : ", email_type)
                                    break
                                if total_leads == int(self.page):
                                    break
                                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                print("Scrolling  for loading more profiles.")
                                try:
                                    self.driver.find_element(By.XPATH,"//span[text()='Next']/..").click()
                                    time.sleep(4)
                                except:pass
                                time.sleep(4)
                                try:
                                    self.driver.find_element(By.XPATH,"//span[text()='More results']/../../..").click()
                                    time.sleep(4)
                                except:
                                    try:
                                        self.driver.find_element(By.XPATH,"//a[@style='transform: scale(1);']").click()
                                        time.sleep(4)
                                    except:pass
                                wait2 = WebDriverWait(self.driver, 5)
                                try:
                                    elements = wait2.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='rso']//h3")))
                                except:
                                    pass
                                for results_no in range(len(elements)):
                                    if total_leads == int(self.page):
                                        break
                                    profile_no += 1
                                    email_count += 2
                                    try:
                                        profile_url = wait2.until(EC.presence_of_element_located((By.XPATH,f"(//div[@class='yuRUbf']//span//a)[{profile_no}]"))).get_attribute('href')
                                    except TimeoutException:
                                        try:
                                            url = f'https://www.google.com/search?q=%22{self.keyword.replace(" ","+")}%22email%3A+%22%40{email_type}%22+site%3Awww.linkedin.com%2Fin%2F+OR+site%3Awww.linkedin.com%2Fpub%2F%221..1000&sca_esv=566068857&cs=0&filter=0&biw=1280&bih=558&dpr=1.5#ip=1'
                                            self.driver.execute_script(f"window.open('{url}')")                                    
                                            self.driver.switch_to.window(self.driver.window_handles[1])
                                            # time.sleep(2000)
                                            time.sleep(4)
                                            WebDriverWait(self.driver, 10).until(
                                                EC.presence_of_element_located((By.XPATH, "//div[@id='recaptcha']"))
                                            )
                                            # time.sleep(1000)
                                            time.sleep(4)
                                            WebDriverWait(self.driver, 20).until(
                                                EC.presence_of_element_located((By.XPATH,f"(//div[@style='-webkit-line-clamp:2'])[1]//span[1]"
                                            )))
                                            time.sleep(4)
                                            self.driver.close()
                                            
                                            self.driver.switch_to.window(self.driver.window_handles[0])
                                            time.sleep(2)
                                            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_UP)
                                            time.sleep(2)
                                            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                            print("Scrolling  for loading more profiles.")
                                            self.driver.switch_to.default_content()
                                            try:
                                                email = self.driver.find_element(By.XPATH,f"(//div[@style='-webkit-line-clamp:2'])[{profile_no}]//span[1]").get_attribute('outerHTML')
                                            except:
                                                hh = False
                                                break
                                            try:
                                                self.driver.find_element(By.XPATH,"//span[text()='Next']/..").click()
                                                time.sleep(4)
                                            except:pass
                                            time.sleep(4)
                                            try:
                                                self.driver.find_element(By.XPATH,"//span[text()='More results']/../../..").click()
                                                time.sleep(4)
                                            except:
                                                try:
                                                    self.driver.find_element(By.XPATH,"//a[@style='transform: scale(1);']").click()
                                                    time.sleep(4)
                                                except:pass
                                            wait2 = WebDriverWait(self.driver, 5)
                                        except TimeoutException:
                                            print("The results are ended for ", email_type)
                                            hh = False
                                            self.driver.close()
                                            self.driver.switch_to.window(self.driver.window_handles[0])
                                            break
                                        
                                        except:
                                            hh = False
                                            break
                                    try:
                                        try:
                                            email = self.driver.find_element(By.XPATH,f"(//div[@style='-webkit-line-clamp:2'])[{profile_no}]//span[1]").get_attribute('outerHTML')
                                        except:
                                            hh = False
                                            break
                                        email = str(email).replace('<em>',"")
                                        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                                        matches = re.findall(email_pattern, email)
                                        email =  str(matches[0])      
                                        try:
                                            email = email.replace(':','')
                                        except:pass
                                        try:
                                            email = email.replace('Id','')
                                        except:pass
                                        try:
                                            email = email.split('&')[0] + email_type
                                        except:pass
                                    except:
                                        email = ''
                                    if email != "":
                                        print("Email  : ", email)
                                        email = email.replace(' ','')
                                        email = email.replace(':','')
                                        email = email.replace('(','')
                                        email = email.replace('to','')
                                        email = email.replace(';','')
                                        email = email.replace(')','')
                                        if ".." not in email and "</span>" not in email:
                                            profiles.append({'linkedin_url': profile_url, 'email': email})
                                            csv_filename = f'output/linkedin_result-{self.keyword}.csv'
                                            email = email.split('@')[0] + "@" + email_type
                                            total_leads += 1
                                            total_leads1 += 1
                                            with open(csv_filename, mode='a', newline='', encoding="utf-8") as f:
                                                writer = csv.writer(f)
                                                writer.writerow([profile_url, email])
                                                print(f"{total_leads} Leads Found ")
                                                print("--------------------------------")
                                

        except TimeoutException:
            print("Page took too long to load. Aborting.")
        finally:
            if self.driver:
                self.driver.quit()
                print("Closed Driver")

if __name__ == "__main__":
    app = App()
    app.start()
