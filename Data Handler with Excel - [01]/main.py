import pandas as pd, csv, datetime, os

try:
    df = pd.read_csv("input.csv")
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y%m%d_%H%M%S')
    filename = f"output_{formatted_datetime}.csv"
    column_headers = [
        "ROLL_RP",
        "book_page",
        "Property_Location",
        "sale_price",
        "City_p",
        "State_p",
        "Zip_p",
        "Owner_Name",
        "Mailing_address_Owner",
        "Mailing_city_Owner",
        "Mailing_state_Owner",
        "Mailing_zip_Owner",
        "PhoneNumber 1",
        "Email 1"
    ]
    print("This will be your output file : ",filename)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(column_headers)

    
    for i in range(len(df["MLSNumber"])):
        roll_rp = df["MLSNumber"].fillna("").get(i)
        book_page = df["Status"].fillna("").get(i)
        property_location = df["Address"].fillna("").get(i)
        sale_price = df["CurrentPrice"].fillna("").get(i)
        city_p = df["City"].fillna("").get(i)
        state_p = df["State"].fillna("").get(i)
        zip_p = df["Zip Code"].fillna("").get(i)
        owner_name = str(df["Owner first name"].fillna("").get(i)) + " " + str(df["Owner last name"].fillna("").get(i))
        Mailing_address_Owner = df[" mailing address,"].fillna("").get(i)
        Mailing_city_Owner = df["mailing city"].fillna("").get(i)
        Mailing_state_Owner = df["mailing state"].fillna("").get(i)
        Mailing_zip_Owner = df["mailing zip"].fillna("").get(i)
        PhoneNumber_1 = df[" phone number"].fillna("").get(i)
        email_1 = df["email"].fillna("").get(i)
        
        with open(f"{filename}", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([roll_rp,book_page,property_location, sale_price, city_p, state_p, zip_p, owner_name,Mailing_address_Owner, Mailing_city_Owner, Mailing_state_Owner, Mailing_zip_Owner, PhoneNumber_1, email_1])
        
    print("Your csv file is ready!")
except:
    print("Your file doesn't exist")
    