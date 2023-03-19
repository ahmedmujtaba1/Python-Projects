from bs4 import BeautifulSoup
import time
import requests

cookies = {
    'x-amz-continuous-deployment-state': 'AYABeJTgj%2FleguDgAz3Vk2zYoWkAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzlQQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADDThSJPhVygtcNdTMAAwLvJmCnTDzxNqJgZ2BrBLQnPhoYauI4%2Fknjt7kc6WgPkn20EWinURknZzutarMBlWAgAAAAAMAAQAAAAAAAAAAAAAAAAAAGEdqSW9AZzqgGZOULeOUrv%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxVLA653zUa2CKqc+KzYCLGJn8Q6OKMMgKrakSi',
    'zguid': '24|%24eb5a0321-b858-4b1c-977a-9b3b21f1ac23',
    'zgsession': '1|8104e75d-5f0f-41a3-9ae2-82a855343681',
    '_ga': 'GA1.2.1354573439.1678599013',
    '_gid': 'GA1.2.1722021624.1678599013',
    'zjs_anonymous_id': '%22eb5a0321-b858-4b1c-977a-9b3b21f1ac23%22',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%22de4e9c60-3a94-4cdb-bbd7-902a91392503%22',
    'pxcts': 'f6812d85-c096-11ed-a1f9-4e5447686677',
    '_pxvid': 'f68121de-c096-11ed-a1f9-4e5447686677',
    '_gcl_au': '1.1.2114602607.1678599013',
    'DoubleClickSession': 'true',
    '_hp2_id.1215457233': '%7B%22userId%22%3A%221595190634666846%22%2C%22pageviewId%22%3A%225653882756349104%22%2C%22sessionId%22%3A%223822581543595954%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    '_hp2_ses_props.1215457233': '%7B%22ts%22%3A1678599015494%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D',
    'x-amz-continuous-deployment-state': 'AYABeLVf4%2FfTqHRHxdUlkjcyL%2FsAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzlQQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADLho1bN+bj4GIXdRYQAwnVqnr9mHAqzuM7nIjQvoplhehLyC+rNCQ3o87RGcFT1zSJedFORHzHeTrXy6mYAgAgAAAAAMAAQAAAAAAAAAAAAAAAAAAKNX3K5ihdp0evcyqNcc1+n%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwziTkIUwC%2FNDWyGhX47g50WsxOMNCAv940qOCyWsxOMNCAv940qOCyWsxOMNCAv940qOCy',
    '__pdst': 'b8e72e929f04478f8b220a05e425a2ba',
    '_fbp': 'fb.1.1678599021788.1275247274',
    '_clck': '152zhoy|1|f9u|0',
    'JSESSIONID': '8CDFC9C7B9DD178E82986C682887E2BB',
    '__gads': 'ID=312b0c44d7fdef05:T=1678599176:S=ALNI_MYUjCdNoUSYN6mvI9qqMci6TipTbQ',
    '__gpi': 'UID=00000bd7abbf3553:T=1678599176:RT=1678599176:S=ALNI_MYW_hbrgDVx9bZNPLKb4YcH7qAtEA',
    '_pin_unauth': 'dWlkPVlUWmhaV1ZsTTJJdE1XWTFOaTAwTVdRMUxXSXhOR1V0T1RNMVlqRXhNemM0TkRJeQ',
    '_px3': '3f6dab026cfc64b7153a9ba57fe3d6b9aad577e918d4f65e73ebb9a8f4341529:A/uwVzUn7K9xqdXNIzLUM+H26657o2IckDGjOf1tBzn7qwoSzzmMpNW0xngPkEzVCn/zBQWcBPQD9JsWZBA1VQ==:1000:lhk3vpQmKedl2znAzrx1S9IETjMit+yz/1Ut8YNlpQkxHA/S4IgJewQemUAwFz/ACR238B/4FQmbLhHGinY6hwVOa/Fedk6spFaQUji5CIczHrKrvQsupwb7QXFbm5MBASKLVqntzjDf9eUp5RQ9rX5Pb1iT2rJ+oDmL1Gc8rrQjvAAUsutenE6Tks8ATSpGw0lsT83q3dgN9jfADIowWA==',
    '_gat': '1',
    '_uetsid': 'fb646ab0c09611edac491d0b5bded7d7',
    '_uetvid': 'fb64b560c09611ed835c354d59d36b72',
    'search': '6|1681192489684%7Crect%3D51.358259735756974%252C-62.12323337499999%252C18.083502567967006%252C-108.70526462499998%26rid%3D44%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26days%3D1%26lt%3Dfsba%252Cfsbo%252Ccmsn%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0924%09%09%09%09%09%09',
    'AWSALB': 'GHP2KMtkjV3BfP9DkEKUpgj7Q6gQXuKRjFgJIZTnhAgzJcY44+XAy1KHQD+hDbBniAaVEyNu0SnH9YQC+okCcMa3HaKokCpUe16hxPHqTbRF3CTByPJsmSHpyfgE',
    'AWSALBCORS': 'GHP2KMtkjV3BfP9DkEKUpgj7Q6gQXuKRjFgJIZTnhAgzJcY44+XAy1KHQD+hDbBniAaVEyNu0SnH9YQC+okCcMa3HaKokCpUe16hxPHqTbRF3CTByPJsmSHpyfgE',
    '_clsk': '1vge4p6|1678600493270|29|0|w.clarity.ms/collect',
}

headers = {
    'authority': 'www.zillow.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'x-amz-continuous-deployment-state=AYABeJTgj%2FleguDgAz3Vk2zYoWkAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzlQQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADDThSJPhVygtcNdTMAAwLvJmCnTDzxNqJgZ2BrBLQnPhoYauI4%2Fknjt7kc6WgPkn20EWinURknZzutarMBlWAgAAAAAMAAQAAAAAAAAAAAAAAAAAAGEdqSW9AZzqgGZOULeOUrv%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAxVLA653zUa2CKqc+KzYCLGJn8Q6OKMMgKrakSi; zguid=24|%24eb5a0321-b858-4b1c-977a-9b3b21f1ac23; zgsession=1|8104e75d-5f0f-41a3-9ae2-82a855343681; _ga=GA1.2.1354573439.1678599013; _gid=GA1.2.1722021624.1678599013; zjs_anonymous_id=%22eb5a0321-b858-4b1c-977a-9b3b21f1ac23%22; zjs_user_id=null; zg_anonymous_id=%22de4e9c60-3a94-4cdb-bbd7-902a91392503%22; pxcts=f6812d85-c096-11ed-a1f9-4e5447686677; _pxvid=f68121de-c096-11ed-a1f9-4e5447686677; _gcl_au=1.1.2114602607.1678599013; DoubleClickSession=true; _hp2_id.1215457233=%7B%22userId%22%3A%221595190634666846%22%2C%22pageviewId%22%3A%225653882756349104%22%2C%22sessionId%22%3A%223822581543595954%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.1215457233=%7B%22ts%22%3A1678599015494%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; x-amz-continuous-deployment-state=AYABeLVf4%2FfTqHRHxdUlkjcyL%2FsAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxMTE2MjczQzlQQzdZU1JDTVBHAAEAAkNEABpDb29raWUAAACAAAAADLho1bN+bj4GIXdRYQAwnVqnr9mHAqzuM7nIjQvoplhehLyC+rNCQ3o87RGcFT1zSJedFORHzHeTrXy6mYAgAgAAAAAMAAQAAAAAAAAAAAAAAAAAAKNX3K5ihdp0evcyqNcc1+n%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAwziTkIUwC%2FNDWyGhX47g50WsxOMNCAv940qOCyWsxOMNCAv940qOCyWsxOMNCAv940qOCy; __pdst=b8e72e929f04478f8b220a05e425a2ba; _fbp=fb.1.1678599021788.1275247274; _clck=152zhoy|1|f9u|0; JSESSIONID=8CDFC9C7B9DD178E82986C682887E2BB; __gads=ID=312b0c44d7fdef05:T=1678599176:S=ALNI_MYUjCdNoUSYN6mvI9qqMci6TipTbQ; __gpi=UID=00000bd7abbf3553:T=1678599176:RT=1678599176:S=ALNI_MYW_hbrgDVx9bZNPLKb4YcH7qAtEA; _pin_unauth=dWlkPVlUWmhaV1ZsTTJJdE1XWTFOaTAwTVdRMUxXSXhOR1V0T1RNMVlqRXhNemM0TkRJeQ; _px3=3f6dab026cfc64b7153a9ba57fe3d6b9aad577e918d4f65e73ebb9a8f4341529:A/uwVzUn7K9xqdXNIzLUM+H26657o2IckDGjOf1tBzn7qwoSzzmMpNW0xngPkEzVCn/zBQWcBPQD9JsWZBA1VQ==:1000:lhk3vpQmKedl2znAzrx1S9IETjMit+yz/1Ut8YNlpQkxHA/S4IgJewQemUAwFz/ACR238B/4FQmbLhHGinY6hwVOa/Fedk6spFaQUji5CIczHrKrvQsupwb7QXFbm5MBASKLVqntzjDf9eUp5RQ9rX5Pb1iT2rJ+oDmL1Gc8rrQjvAAUsutenE6Tks8ATSpGw0lsT83q3dgN9jfADIowWA==; _gat=1; _uetsid=fb646ab0c09611edac491d0b5bded7d7; _uetvid=fb64b560c09611ed835c354d59d36b72; search=6|1681192489684%7Crect%3D51.358259735756974%252C-62.12323337499999%252C18.083502567967006%252C-108.70526462499998%26rid%3D44%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26days%3D1%26lt%3Dfsba%252Cfsbo%252Ccmsn%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0924%09%09%09%09%09%09; AWSALB=GHP2KMtkjV3BfP9DkEKUpgj7Q6gQXuKRjFgJIZTnhAgzJcY44+XAy1KHQD+hDbBniAaVEyNu0SnH9YQC+okCcMa3HaKokCpUe16hxPHqTbRF3CTByPJsmSHpyfgE; AWSALBCORS=GHP2KMtkjV3BfP9DkEKUpgj7Q6gQXuKRjFgJIZTnhAgzJcY44+XAy1KHQD+hDbBniAaVEyNu0SnH9YQC+okCcMa3HaKokCpUe16hxPHqTbRF3CTByPJsmSHpyfgE; _clsk=1vge4p6|1678600493270|29|0|w.clarity.ms/collect',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}
import json
url = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A43.229426333199925%2C%22east%22%3A-73.76874118749998%2C%22south%22%3A29.075652527756542%2C%22west%22%3A-97.05975681249998%7D%2C%22mapZoom%22%3A5%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A24%2C%22regionType%22%3A2%7D%2C%7B%22regionId%22%3A53%2C%22regionType%22%3A2%7D%2C%7B%22regionId%22%3A22%2C%22regionType%22%3A2%7D%2C%7B%22regionId%22%3A4%2C%22regionType%22%3A2%7D%2C%7B%22regionId%22%3A44%2C%22regionType%22%3A2%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22doz%22%3A%7B%22value%22%3A%221%22%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22],%22cat2%22:[%22total%22]}&requestId=3'
response = requests.get(
    url,
    cookies=cookies,
    headers=headers,
)
jj_data=json.loads(response.text)
list_data=jj_data['cat1']['searchResults']['listResults']
da=[]
for link in list_data[0:1]:
    da.append(link['detailUrl'])
for i in da:
    response2 = requests.get(i,
    cookies=cookies,
    headers=headers,)
    soup2 = BeautifulSoup(response2.text, "lxml")
    print(i)
    
    price = soup2.find("span", class_= "Text-c11n-8-84-0__sc-aiai24-0 dpf__sc-1me8eh6-0 hLAJE fzJCbY").text
    print(price)
    bed = soup2.find_all("span", class_= 'Text-c11n-8-84-0__sc-aiai24-0 fsXIkY')[0].text.split(' ')[0]
    print(bed)
    bathroom = soup2.find_all("span", class_= 'Text-c11n-8-84-0__sc-aiai24-0 fsXIkY')[1].text.split(' ')[0]
    print(bathroom)
    area = soup2.find_all("span", class_= 'Text-c11n-8-84-0__sc-aiai24-0 fsXIkY')[2].text
    print(area)
    address = soup2.find("h1", class_= 'Text-c11n-8-84-0__sc-aiai24-0 fsXIkY').text
    print(address)
    state = soup2.find("h1", class_= 'Text-c11n-8-84-0__sc-aiai24-0 fsXIkY').text.split(',')[2].strip().split(' ')[0]
    print(state)
    zes = soup2.find("span", class_= 'Text-c11n-8-84-0__sc-aiai24-0 gTVYcr').text
    if '$' in zes:
        zestimate = zes
        print(zestimate)
    else:

        zestimate = 'none'
        print(zestimate)
    home_type = soup2.find_all("span", class_= 'Text-c11n-8-84-0__sc-aiai24-0 dpf__sc-2arhs5-3 fsXIkY btxEYg')[0].text
    print(home_type)
    build_in = soup2.find_all("span", class_= 'Text-c11n-8-84-0__sc-aiai24-0 dpf__sc-2arhs5-3 fsXIkY btxEYg')[1].text.split(' ')[-1]
    print(build_in)
    data = soup2.find_all("span", class_= 'Text-c11n-8-84-0__sc-aiai24-0 dpf__sc-2arhs5-3 fsXIkY btxEYg')
    for i in data:
        try:
            if 'price/sqft' in i.text:
                price_per_sqrft = i.text
                print(price_per_sqrft)
        except:
            price_per_sqrft = 'none'
            print(price_per_sqrft)
    name = soup2.find_all("p", class_= "Text-c11n-8-84-0__sc-aiai24-0 fsXIkY")[1].text
    print(name)

    print("==============================================")
        


 