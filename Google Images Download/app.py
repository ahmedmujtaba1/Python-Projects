import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep as wait
from selenium.webdriver.common.by import By
import requests
import base64

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
df = pd.read_excel('data.xls')
cnt = 115
for i in range(len(df["Artikelnr;Omschrijving;Merk;Eenheid;Inhoud-1;Verpakking-1;Statiegeld-1;EAN-1;Inhoud-2;Verpakking-2;Statiegeld-2;EAN-2;Inhoud-3;Verpakking-3;Statiegeld-3;EAN-3;Prijs;BestelPer;VBR;Adviesprijs;AktieStart;AktieEind;Aktieprijs;BTW;KortingVanaf;Alcohol%"])):
    product_name = df["Artikelnr;Omschrijving;Merk;Eenheid;Inhoud-1;Verpakking-1;Statiegeld-1;EAN-1;Inhoud-2;Verpakking-2;Statiegeld-2;EAN-2;Inhoud-3;Verpakking-3;Statiegeld-3;EAN-3;Prijs;BestelPer;VBR;Adviesprijs;AktieStart;AktieEind;Aktieprijs;BTW;KortingVanaf;Alcohol%"][cnt]
    print("[+] Product to search is " +  str(product_name))
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    product_name = str(product_name).replace('/', ' ')
    product_name = str(product_name).replace('*', ' ')
    product_name = str(product_name).replace(' ', ' ')
    path = f'./images/{product_name}.png'
    url = f"https://www.google.com/search?q={product_name}&tbm=isch&ved=2ahUKEwivqPva-p7_AhVtpycCHSEcAmkQ2-cCegQIABAA&oq=116100%3BFILLIERS+Advokaat+Weckpot%3BFILLIERS%3BLTR%3B.2%3BSET%3B0%3B5415200003242%3B6%3BDOOS%3B0%3B05415200003259%3B0%3B%3B0%3B%3B4.8%3B1%3B0%3B7.95%3B01%2F04%2F23%3B31%2F05%2F23%3B4.55%3BH%3B0%3B14&gs_lcp=CgNpbWcQA1DAAljVBWCmB2gAcAB4AIABAIgBAJIBAJgBAKABAaoBC2d3cy13aXotaW1nsAEAwAEB&sclient=img&ei=Ge12ZO-3MO3OnsEPobiIyAY&bih=609&biw=1280&rlz=1C1VDKB_enPK1054PK1055&safe=active&ssui=on#imgrc=SzrjngwmvLoZOM"
    driver.get(url)
    wait(10)
    cnt += 1
    img_url = driver.find_element(By.XPATH,"(//img[@class='rg_i Q4LuWd'])[1]")
    if (img_url.get_attribute('src') is not None):
            my_image = img_url.get_attribute('src').split('data:image/jpeg;base64,')
            if(len(my_image) >1): 
                with open(path, 'wb') as f: 
                    f.write(base64.b64decode(my_image[1])) 
                    print('Image Downloaded Successfully') 
                    print("-------------------------------------------------------------------------")

