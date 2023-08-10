import requests, csv
from bs4 import BeautifulSoup

page = 1
total_products = 0
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Link", "Price", "Model", "Make", "Year", "Mileage", "Steering Side", "Seller Name", "Trim", "Regional Specs", "Warranty"
        , "Exterior Color", "Body Collection", "Body Type", "Mechanical Condition", "Cylinder", "Transmission Type", "Horsepower", "Fuel Type", "Description"])
for i in range(1000):
    headers = {
        "Authority" : "dubai.dubizzle.com",
        "Method"  : "GET",
        "Path" : f"/motors/used-cars/?page={page}",
        "Scheme" : "https",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent"  : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0",
    }
    r = requests.get(f"https://dubai.dubizzle.com/motors/used-cars/?page={page}", headers=headers)
    print(f"https://dubai.dubizzle.com/motors/used-cars/?page={page}")
    soup = BeautifulSoup(r.content, 'html.parser')
    price_container = soup.find_all('div', attrs={"data-testid" : "listing-price"})
    make_container = soup.find_all('div', attrs={"data-testid" : "heading-text-1"})
    model_container = soup.find_all('div', attrs={"data-testid" : "heading-text-2"})
    year_container = soup.find_all('div', attrs={"data-testid" : "listing-year"})
    mileage_container = soup.find_all('div', attrs={"data-testid" : "listing-kms"})
    seller_name_container = soup.find_all('img', attrs={"data-testid" : "dealer-logo"})
    steering_side_container = soup.find_all('div', attrs={"data-testid" : "listing-steering side"})
    cnt = 0
    for d in range(len(price_container)):
        cnt += 1
        total_products += 1
        try:
            link = "https://dubai.dubizzle.com" + str(soup.find('a', attrs={"data-testid" : f"listing-{cnt}"})['href']) + "/"
            price = price_container[cnt].text
            make = make_container[cnt].text
            model = model_container[cnt].text
            year = year_container[cnt].text
            mileage = mileage_container[cnt].text
            try:
                seller_name = seller_name_container[cnt]['alt']
            except:
                seller_name = "N/A"
            steering_side = steering_side_container[cnt].text
            headers2 = {
                "Authority" : "dubai.dubizzle.com",
                "Method" : "GET",
                "Path" : f'{str(soup.find("a", attrs={"data-testid" : f"listing-{cnt}"})["href"])}/',
                "Scheme" : "https",
                "max-age" : "0",
                "Accept" : "text/html",
                # "Accept-Encoding" : "gzip, deflate, b",
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0", 
            }
            r2 = requests.get(f"{link}", headers=headers2)
            soup1 = BeautifulSoup(r2.content, 'html.parser')
            try:
                trim = soup1.find("p", attrs={"data-ui-id" : "details-value-motors_trim"}).text
            except:trim = 'N/A'
            try: 
                regional_specs = soup1.find("p", attrs={"data-ui-id" : "details-value-regional_specs"}).text
            except:regional_specs = 'N/A'
            try:
                warranty = soup1.find("p", attrs={"data-ui-id" : "details-value-warranty"}).text
            except:warranty = 'N/A'
            exterior_color = soup1.find("p", attrs={"data-ui-id" : "details-value-exterior_color"}).text
            body_collection = soup1.find("p", attrs={"data-ui-id" : "details-value-body_condition"}).text
            body_type = soup1.find("p", attrs={"data-ui-id" : "details-value-body_type"}).text
            mechanical_condition = soup1.find("p", attrs={"data-ui-id" : "details-value-mechanical_condition"}).text
            cylinder = soup1.find("p", attrs={"data-ui-id" : "details-value-no_of_cylinders"}).text
            transmission_type = soup1.find("p", attrs={"data-ui-id" : "details-value-transmission_type"}).text
            horsepower = soup1.find("p", attrs={"data-ui-id" : "details-value-horsepower"}).text
            fuel_type = soup1.find("p", attrs={"data-ui-id" : "details-value-fuel_type"}).text
            description_container = soup1.find("div", attrs={"class" : "sc-1bi45uo-2 FSTMI"})
            description = []
            description1 = description_container.find_all('span')[0].text
            description2 = description_container.find_all('span')[1].text
            description.append(description1)
            description.append(description2)
            car_accident = "Not Avaliable"

            print("Link : ", link)
            print("price : ", price)
            print("Make : ", make)
            print("Model : ", model)
            print("Year Model : ", year)
            print("Mile Age Reading : ", mileage)
            print("Steering Side : ", steering_side)
            print("Seller Name : ", seller_name)
            print("Trim : ", trim)
            print("Regional Specs : ", regional_specs)
            print("Warranty : ", warranty)
            print("Exterior Color: ", exterior_color)
            print("Body Type: ", body_type)
            print("Body Collection: ", body_collection)
            print("Mechnical Condition: ", mechanical_condition)
            print("No of cylinders: ", cylinder)
            print("Transmission Type: ", transmission_type)
            print("HorsePower: ", horsepower)
            print("Fuel Type: ", fuel_type)
            # print("Fuel Type: ", fuel_type)
            print("Description: ", description)
            print("Total Products : ", total_products)
            print("--------------------------------------------------")
            with open("data.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([
                    link, price, model, make, year, mileage, steering_side, seller_name, trim, regional_specs, warranty
                    , exterior_color, body_collection, body_type, mechanical_condition, cylinder, transmission_type, horsepower, fuel_type, description])
        except:
            page += 1
            pass
            





    