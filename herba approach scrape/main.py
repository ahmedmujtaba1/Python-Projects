#Imports
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
class Scraper():
    def __init__(self):
        self.main = 0
        self.page_no = 0
        self.product = 0

    def wait(self, times):
        time.sleep(int(times)) #miliseconds

    def opening_chrome(self):
        self.chrome_options = uc.ChromeOptions()
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-infobars')

        self.url = input(str("Your Url : "))
        print("[+] Opening Chrome")
        self.driver = uc.Chrome(options=self.chrome_options)
        print("[+] Requesting website. Waiting for response")
        self.wait(1)
        print("[+] Finally Get 200 status code.")
        self.driver.get(self.url)

    def writing_csv(self):
        with open('herba_approach_scraper.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Title','Product Link','Short Description',"Off {Sale}",'Long Description', "Category", "Reviews","Size1","Price1","Size2","Price2","Size3","Price3","Size4","Price4"])

   
    def locating_landing_page(self):
        self.opening_chrome()
        print("[+] Waiting for 7 miliseconds")
        self.wait(12)

    def get_product_details(self):
        self.product_list = self.driver.find_elements(By.XPATH,f"//a[text()='Add to cart']/../..//div[@class='name product-title woocommerce-loop-product__title']//a")
        # print(len(self.product_list))
        for n in range(len(self.product_list)):
            print("Scraping Details")
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            print(self.product)
            try:
                self.products = self.product_list[self.product]
            except:break
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            self.product += 1
            self.product_link = self.products.get_attribute('href')
            self.products.click()
            self.wait(4)
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[2]").click()
            except:pass
            self.product_title = self.driver.find_element(By.XPATH,"//h1[@class='product-title product_title entry-title']").text
            self.cate = self.driver.find_elements(By.XPATH,"//nav[@class='woocommerce-breadcrumb breadcrumbs uppercase']//a")
            self.category = f"{str(self.cate[1].text)}/{str(self.cate[2].text)}/{str(self.product_title)}"
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            try:
                self.size1 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[1]").text
                self.price1 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[2]").text
            except:
                self.size1 = ""
                self.price1 = self.driver.find_element(By.XPATH,"//span[@class='reg_price']//span//bdi").text
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            try:
                self.size2 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[6]").text
                self.price2 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[7]").text
            except:
                self.size2 = ""
                self.price2 = ""
            try:
                self.size3 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[11]").text
                self.price3 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[12]").text
            except:
                self.size3 = ""
                self.price3 = ""
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            try:

                self.size4 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[16]").text
                self.price4 = self.driver.find_element(By.XPATH,"(//div[@class='isw-term isw-enabled']//span)[17]").text
            except:
                self.price4 = ""
                self.size4 = ""
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            # self.quantity = str(self.driver.find_element(By.XPATH,"//div[@class='quantity buttons_added']//input[@name='quantity']").get_attribute('max'))
            try:
                self.short_description = self.driver.find_element(By.XPATH,"//div[@class='box-description box-label']//p").text
            except:self.short_description = ""
            try:
                self.long_description = self.driver.find_element(By.ID,"tab-description").text
            except:
                self.long_description = ""
            try:
                self.driver.find_element(By.XPATH,"(//button[@class='needsclick klaviyo-close-form kl-private-reset-css-Xuajs1'])[1]").click()
            except:pass
            self.reviews = self.driver.find_element(By.XPATH,"//li[@id='tab-title-reviews']//a").text
            try:
                self.off = self.driver.find_element(By.XPATH,"(//span[@class='onsale']//span//bdi)[1]").text
            except: 
                self.off = "Not Avaliable on this product"
            # print(self.product_title,self.product_link, self.short_description, self.off, self.long_description, self.category, self.reviews, self.size1, self.price1, self.size2, self.price2, self.size3, self.price3, self.size4, self.price4)
            self.driver.back()
            with open('herba_approach_scraper.csv', 'a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([self.product_title,self.product_link, self.short_description, self.off, self.long_description, self.category, self.reviews, self.size1, self.price1, self.size2, self.price2, self.size3, self.price3, self.size4, self.price4])
            self.wait(4)
            # self.wait(50)
            try:
                self.driver.find_element(By.XPATH,"//button[@title='Close (Esc)']").click()
            except:pass
    def main_category_handlers(self):
        pagination = self.driver.find_elements(By.XPATH,"//ul[@class='page-numbers nav-pagination links text-center']//li")
        # print(f"[+] There are {len(pagination)-1} pages.")
        cnt = 4
        for page in range(len(pagination)+50):
            self.product = 0
            try:
                try:
                    self.get_product_details()
                except:pass
                self.wait(2)
                self.driver.get(f"{self.url}page/{cnt}/")
                self.wait(5)
                self.get_product_details()
                cnt += 1
            except:
                print("[+] Quiting")
                cnt = 0
                
                break

        # self.get_product_details()
    def start(self):
        # self.writing_csv()
        self.main = 1
        print("[+] Hello, I am the bot.")
        self.locating_landing_page()
        self.main_category_handlers()
scraper = Scraper()
scraper.start()