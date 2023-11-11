import requests
from bs4 import BeautifulSoup as bs
for page_no in range(1, 10):
    print(f'[+] Moving to Page no [{page_no}]')
    my_url = f'https://www.answers.com/other-business?page={page_no}'
    r = requests.get(my_url)
    content = bs(r.content, 'html.parser')
    products = content.find_all('div', attrs={'class':'body2 mb-2 text-primaryColor'})
    for i in range(0, len(products)):
        product_title = content.find_all('div', attrs={'class':'body2 mb-2 text-primaryColor'})[i].text
        num_of_ans = content.find_all('div', attrs={'class':'caption1'})[i].text
        ans_link = content.find_all('div', attrs={'class' : 'border border-solid border-primaryLight rounded-md cursor-pointer p-4 m-4'})[i].find('a')['href']
        print(product_title+ "?")
        print("Answer : ",num_of_ans)
        print("Link : ", ans_link) 
        print('---------------------------------------------------')