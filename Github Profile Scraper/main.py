import requests
from PIL import Image   
from bs4 import BeautifulSoup as bs

r = requests.get("https://github.com/hammad-air")
if r.status_code == 200:
    soup = bs(r.content, 'html.parser')
    name = str(soup.find('span', attrs={'itemprop':'name'}).text).replace('\n','').lstrip()
    username = str(soup.find('span', attrs={'itemprop':'additionalName'}).text).replace('\n','').lstrip()
    bio = soup.find('div', attrs={'class':'p-note user-profile-bio mb-3 js-user-profile-bio f4'})['data-bio-text'].lstrip()
    image_url = soup.find('a', attrs={'itemprop':'image'}).find('img')['src']
    print("Name : ",name)
    print("Username : ",username)
    print("Bio : ",bio)
    print("Image Url : ",image_url)
    img_data = requests.get(image_url).content
    path_image = f"img/github-{username}.jpg"
    with open(path_image, 'wb') as handler:
        handler.write(img_data)
    
    
