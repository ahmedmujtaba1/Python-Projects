from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time, requests, pickle, csv, random, tkinter as tk
from email_check_scraper import email_checker
from tkinter import ttk
from ttkthemes import ThemedStyle

class CustomTkinterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("LinkedIn Email Scraper")
        self.root.geometry("800x400")
        self.style = ThemedStyle(self.root)
        self.style.set_theme("plastik")
        self.root.configure(bg="#1E90FF")

        self.title_label = tk.Label(self.root, text="LinkedIn Email Scraper", font=("Helvetica", 18), fg="white", bg="#1E90FF")
        self.title_label.pack(pady=(20, 0))
        self.create_widgets()
        self.emails = []

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Blue.TLabel", foreground="white", font=("Helvetica", 12))

        self.root.configure(bg="blue")

        title_label = tk.Label(self.root, text="Made By Mohsin Haroon", font=("Helvetica", 16, "bold"), bg="blue", fg="white")
        title_label.pack(pady=10, padx=10, anchor="w")

        keyword_frame = tk.Frame(self.root, bg="blue")
        keyword_frame.pack(pady=10, padx=10, anchor="w")

        lblKeyword = tk.Label(keyword_frame, text="Keyword", font=("Helvetica", 12), bg="blue", fg="white")
        lblKeyword.pack(side="left", padx=(0, 10))

        self.keyword = tk.StringVar()
        self.tbKeyword = tk.Entry(keyword_frame, textvariable=self.keyword, font=("Helvetica", 12))
        self.tbKeyword.pack(side="left")

        page_frame = tk.Frame(self.root, bg="blue")
        page_frame.pack(pady=10, padx=10, anchor="w")

        lblPage = tk.Label(page_frame, text="Page Number", font=("Helvetica", 12), bg="blue", fg="white")
        lblPage.pack(side="left", padx=(0, 10))

        self.page = tk.StringVar()
        self.tbPage = tk.Entry(page_frame, textvariable=self.page, font=("Helvetica", 12))
        self.tbPage.pack(side="left")

        location_frame = tk.Frame(self.root, bg="blue")
        location_frame.pack(pady=10, padx=10, anchor="w")

        lblLocation = tk.Label(location_frame, text="Location", font=("Helvetica", 12), bg="blue", fg="white")
        lblLocation.pack(side="left", padx=(0, 10))

        countries = ["Select Country", "United States", "Canada", "United Kingdom", "Australia", "Other"]
        self.location = tk.StringVar()
        self.location.set("Select Country")
        self.location_dropdown = ttk.Combobox(location_frame, textvariable=self.location, values=countries, font=("Helvetica", 12))
        self.location_dropdown.pack(side="left")

        style.configure("Blue.TButton", font=("Helvetica", 12), foreground="white")
        self.btnGetEmails = ttk.Button(self.root, text="Get Emails", style="Blue.TButton", command=self.GetProfiles)
        self.btnGetEmails.pack(pady=10, padx=10, anchor="e")
        self.selected_country = self.location.get()

    def run(self):
        self.root.mainloop()

    def GetProfiles(self):
        try:
            self.chrome_options = webdriver.ChromeOptions()
            self.chrome_options.add_argument("--disable-notifications")
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver.maximize_window()
            self.keyword = self.keyword.get()
            self.page = self.page.get()
            # Login
            self.driver.get("https://www.linkedin.com/")
            with open('cookies.pkl', 'rb') as f:
                cookies = pickle.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()
            self.url = f"https://www.linkedin.com/search/results/PEOPLE/?keywords={str(self.keyword).replace(' ', '%20')}&origin=SWITCH_SEARCH_VERTICAL&sid=g2w"
            self.driver.get(self.url)
            time.sleep(2)

            profiles = []
            pages = int(self.page)
            total_page_no = 1

            csv_filename = f'output/linkedin_result-{self.keyword}.csv'
            with open(csv_filename, mode='w', newline='', encoding="utf-8") as csv_file:
                fieldnames = ['linkedin_url', 'email']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

            while total_page_no <= pages:
                wait = WebDriverWait(self.driver, 10)
                time.sleep(2)
                wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                time.sleep(1)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

                profileDivs = self.driver.find_elements(By.XPATH, "//div[@class='t-roman t-sans']")

                cnt = 0
                for div in profileDivs:
                    cnt += 1
                    profile_url = self.driver.find_element(By.XPATH, f"(//div[@class='t-roman t-sans']//a)[{cnt}]").get_attribute("href").split('?miniProfileUrn')[0]
                    if "search/results" not in profile_url:
                        print("Adding this Profile Link : ", profile_url)
                        try:
                            profile_name = self.driver.find_element(By.XPATH, f"(//div[@class='t-roman t-sans']//a//span[@dir='ltr']//span[@aria-hidden='true'])[{cnt}]").text
                            email_types = [
                                "yahoo.com",
                                "hotmail.com",
                                "outlook.com",
                            ]
                            choices = [1,2,3,2,3,4,2,1,3,2,1,2,3,4,3,2,1,1,2,3]
                            choice = int(random.choice(choices))
                            email_format = ""
                            if choice == 1:
                                email_format = profile_name.split(' ')[0].lower() + "_" + profile_name.split(' ')[1].lower() + str(random.randint(1,100))
                            elif choice == 2:
                                email_format = profile_name.split(' ')[1].lower() + "_" + profile_name.split(' ')[0].lower() + str(random.randint(1,100))
                            elif choice == 3:
                                email_format = profile_name.split(' ')[0].lower() + profile_name.split(' ')[1].lower() + str(random.randint(1,100))
                            elif choice == 4:
                                personal_emails = profile_name.split(' ')[0].lower() + profile_name.split(' ')[1].lower() + str(random.randint(1,100)) + "@gmx.com"
                            if email_format.endswith('@gmx.com') == False:
                                personal_emails = f"{email_format}@{random.choice(email_types)}"
                            if profile_name:
                                profiles.append({'linkedin_url': profile_url, 'email': personal_emails})
                            else:
                                profiles.append({'linkedin_url': profile_url, 'email': ''})
                        except:profile_name = None

                btnNext = self.driver.find_element(By.XPATH, "//button[@aria-label='Next']")
                if btnNext and not "artdeco-button--disabled" in btnNext.get_attribute("class"):
                    self.driver.execute_script("arguments[0].click();", btnNext)
                    total_page_no += 1
                    cnt = 0
                    print(f"Moving to Page {total_page_no}")
                    print("-------------------------------------------")
                else:
                    break

            # if profiles:
            #     with open(f'output/linkedin_result-{self.keyword}.csv', mode='w', newline='') as csv_file:
            #         fieldnames = ['linkedin_url', 'email']
            #         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            #         writer.writeheader()
            #         for profile in profiles:
            #             if profile['email']:  # Only write rows with non-empty emails
            #                 writer.writerow(profile)
            #     print(f'output/linkedin_result-{self.keyword}.csv file saved successfully.')
            # else:
                with open(f'output/linkedin_result_with_email-{self.keyword}.csv', mode='w', newline='', encoding="utf-8") as csv_file:
                    fieldnames = ['linkedin_url', 'email']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for profile in profiles:
                        writer.writerow(profile)

        except TimeoutException:
            print("Page took too long to load. Aborting.")
        finally:
            if self.driver:
                self.driver.quit()
                print("Closed Driver")

if __name__ == "__main__":
    app = CustomTkinterApp()
    app.run()
