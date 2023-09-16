import os, re
import pandas as pd
import numpy as np
from datetime import datetime



def process_input_file_type_2(input_file, file_name):
    try:
        input_df = pd.read_csv("input/" + str(input_file))
    except FileNotFoundError:
        print(f"File not found: {input_file}")
        return

    columns_to_include = [
        "First Name",
        "Middle Name",
        "Last Name",
        "Prefix",
        "Suffix",
        "Full Legal Name",
        "About",
        "Birthday",
        "Home Anniversary",
        "Cell Phone",
        "Is Primary? (Mark Y)",
        "Home Phone",
        "Is Primary? (mark Y)",
        "Work Phone",
        "Is Primary? (mark Y)",
        "Other Phone",
        "Is Primary? (mark Y)",
        "Personal Email",
        "Primary? (MArk Y)",
        "Work Email",
        "Primary? (mark Y)",
        "Other Email",
        "Primary? (mark Y)",
        "Address line one",
        "Address line two",
        "City",
        "State",
        "Zip code",
        "Country",
        "Label",
        "Address line one",
        "Address line two",
        "City",
        "State",
        "Zip code",
        "Country",
        "Label",
        "Address line one",
        "Address line two",
        "City",
        "State",
        "Zip code",
        "Country",
        "Label",
        "Tags",
        "Source",
        "Notes",
        "Facebook",
        "Twitter",
        "Linkedin",
        "Pinterest",
        "Instagram",
    ]

    output_df = pd.DataFrame(columns=columns_to_include)
    output_df["Notes"] = notes
    try:
        output_df["First Name"] = input_df["Owner Label Name"].apply(lambda x: x.split(' ')[0].strip().lower().capitalize() if pd.notna(x) and ' ' in x else '')
    except: output_df["First Name"] = ''
    try:
        output_df["Last Name"] = input_df["Owner Label Name"].apply(lambda x: x.split(' ')[-1].strip().lower().capitalize() if pd.notna(x) and ' ' in x else '')
    except:output_df["Last Name"]
    try:
        output_df["Full Legal Name"] = input_df["Current Owner Name"].apply(lambda x: x.strip().lower().capitalize() if pd.notna(x) else '')
    except: output_df["Full Legal Name"] = ''

    if "PhoneNumber 1" in input_df.columns:
        output_df["Cell Phone"] = np.where(
            input_df["Status"].str.lower() == "call",
            input_df["PhoneNumber 1"],
            ""
        )
        
        output_df["Is Primary? (Mark Y)"] = np.where(
            (input_df["Status"].str.lower() == "call") & pd.notna(input_df["PhoneNumber 1"]) & (input_df["PhoneNumber 1"] != ""),
            "Y",
            ""
        )

    if "Email 1" in input_df.columns:
        output_df["Personal Email"] = np.where(
            (input_df["ZB Status"].str.lower() == "valid") & pd.notna(input_df["Email 1"]) & (input_df["Email 1"] != ""),
            input_df["Email 1"],
            ""
        )

        output_df["Primary? (MArk Y)"] = np.where(
            (input_df["ZB Status"].str.lower() == "valid") & pd.notna(input_df["Email 1"]) & (input_df["Email 1"] != ""),
            "Y",
            ""
        )

    if "Property Address Formatted" in input_df.columns:
        output_df["Address line one"] = input_df["Property Address Formatted"]

    if "City" in input_df.columns:
        city_and_state = input_df["City"].str.rsplit(" ", 1)
        if city_and_state.str.len().eq(2).all():
            output_df["City"] = city_and_state.str[0]
            output_df["State"] = city_and_state.str[1]
        else:
            output_df["City"] = input_df["City"]

    if "Postal Code" in input_df.columns and "Owner Carrier Route" in input_df.columns:
        postal_code = input_df["Postal Code"].astype(str)
        carrier_route = input_df["Owner Carrier Route"].apply(lambda x: "-" + str(x) if pd.notna(x) and x != "" else "")
        
        zip_code = postal_code + carrier_route
        cleaned_zip_code = []
        
        for code in zip_code:
            if str(code).endswith(' ') == True:
                cleaned_zip_code.append(str(code).replace('-', '')) 
                # print("Error Code : ", code)
            else:
                cleaned_zip_code.append(code)

        output_df["Zip code"] = cleaned_zip_code
    output_df["Label"] = "Property Address"
    output_df["Tags"] = "BL-Referral"

    output_df = output_df[(pd.notna(output_df["Cell Phone"]) & (output_df["Cell Phone"] != "")) |
                      (pd.notna(output_df["Personal Email"]) & (output_df["Personal Email"] != ""))]

    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)

    output_file_timestamp = os.path.join(output_folder, file_name)
    output_df.to_csv(output_file_timestamp, index=False)


def process_input_file(input_file, file_name):
    input_df = pd.read_csv("input/" + str(input_file))

    def check_absentee(row):
        property_address = re.sub(
            r"\s+", "", str(row.get("Property Address Formatted", ""))
        ).lower()
        owner_address = re.sub(r"\s+", "", str(row.get("Owner Address", ""))).lower()
        if property_address == owner_address:
            return "OO"
        else:
            return "Absentee"

    def check_owner_type(row):
        owner_name = str(row.get("Current Owner Name", "")).lower()
        with open("include/business.txt", "r") as business_file:
            business_keywords = [line.strip().lower() for line in business_file]
        with open("include/trust.txt", "r") as trust_file:
            trust_keywords = [line.strip().lower() for line in trust_file]
        if any(keyword in owner_name for keyword in business_keywords):
            return "Business"
        elif any(keyword in owner_name for keyword in trust_keywords):
            return "Trust"
        else:
            return "Person"

    def check_multiple_properties(row):
        owner_name = str(row.get("Current Owner Name", "")).lower()
        owner_address = str(row.get("Owner Address", "")).lower()
        d = str(row.get("Current Owner Name", "")).lower()

        # Check if 'Owner Address' is in the columns of input_df
        if "Owner Address" in input_df.columns:
            matching_properties = input_df[
                (d == owner_name)
                & (input_df["Owner Address"].str.lower() == owner_address)
            ]
        else:
            matching_properties = pd.DataFrame()  # Create an empty DataFrame

        if len(matching_properties) > 1:
            return "Yes"
        else:
            return "No"

    input_df["Absentee"] = input_df.apply(check_absentee, axis=1)
    input_df["Owner-Type"] = input_df.apply(check_owner_type, axis=1)
    # input_df["Multiple properties"] = input_df.apply(check_multiple_properties, axis=1)

    global notes
    try:
        sale_amount = input_df['Sale Amount'].apply(lambda x: f"${x}" if not pd.isna(x) else '')
    except:sale_amount = ''
    try:    
        property_class = input_df['Property Class'].str.lower().str.capitalize()
    except:property_class = ''
    try:

        input_df['Settle Date'] = pd.to_datetime(input_df['Settle Date'], errors='coerce').dt.strftime('%d/%m/%Y')
        settle_date = input_df['Settle Date']
    except: 
        settle_date = ''
    try:
        county = input_df['County'].str.lower().str.capitalize()
    except:county = ''
    input_df['Absentee'] = input_df.apply(check_absentee, axis=1)
    input_df['Multiple Properties'] = input_df.apply(check_multiple_properties, axis=1)

    absentee_values = input_df['Absentee']
    multiple_properties_values = input_df['Multiple Properties']

    notes = (
        "Sale amount: " + sale_amount +
        " - Settle date: " + settle_date +
        " - County: " + county +
        " - Property class: " + property_class +
        " - Absentee: " + absentee_values +
        " - Multiple properties: " + multiple_properties_values
    )
    
    # print("Notes: ", notes)

    input_df["Notes"] = notes



    try:
        input_df = input_df[
            ((input_df["Status"] == "Call") | input_df["Status"].isna())
            & ((input_df["ZB status"] == "Valid") | input_df["ZB status"].isna())
        ]
    except KeyError:
        pass

    
    # input_df["Cell Phone"] = input_df.get("PhoneNumber 1", "")
    # input_df["Is Primary? (mark Y)"] = input_df["Cell Phone"].apply(
    #     lambda x: "Y" if not pd.isna(x) else ""
    # )
    # input_df["Personal Email"] = input_df.get("Email 1", "")
    # input_df["Primary? (mark Y)"] = input_df["Cell Phone"].apply(
    #     lambda x: "Y" if not pd.isna(x) else ""
    # )

    # # Handle 'City' column format
    # input_df["City"] = input_df["City"].apply(
    #     lambda x: x.rsplit(" ", 1)[0] if isinstance(x, str) and " " in x else x
    # )
    # input_df["State"] = input_df["City"].apply(
    #     lambda x: x.rsplit(" ", 1)[1] if isinstance(x, str) and " " in x else ""
    # )

    # # Generate 'Zip code' based on conditions
    # input_df["Zip code"] = input_df.apply(
    #     lambda row: f"{row.get('Postal code', '')}{'-' + row.get('Owner carrier route', '') if not pd.isna(row.get('Owner carrier route', '')) else ''}",
    #     axis=1,
    # )

    # input_df["Label"] = "Property Address"
    # input_df["Tags"] = "BL-Referral"

    # Define output folder and save the processed DataFrame
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    output_file_timestamp = os.path.join(output_folder, file_name)

    input_df.to_csv(output_file_timestamp, index=False)


input_folder = "input/"
csv_files = [file for file in os.listdir(input_folder) if file.endswith(".csv")]
for file in csv_files:
    file = str(file)
    name_file = file.replace(" ", "_")
    name_file = file.replace(".csv", "-")
    name_file = file.replace("-", "_")
    print("Name File : ", name_file.split(".csv")[0])
    print("Name File2  : ", file)
    filename_output = (
        f"{name_file.split('.csv')[0]}_Format1_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )
    filename_output2 = (
        f"{name_file.split('.csv')[0]}_Format2_"
        + datetime.now().strftime("%Y%m%d")
        + ".csv"
    )
    process_input_file(file, filename_output)
    process_input_file_type_2(file, filename_output2)
