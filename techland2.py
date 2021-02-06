from bs4 import BeautifulSoup
import requests







casing = 'https://www.techlandbd.com/pc-components/computer-casing'
#processor = "https://www.startech.com.bd/component/processor"
result = requests.get(casing)
src = result.content

soup = BeautifulSoup( src , 'lxml')
#print(soup)
container = soup.find("div", {"class":"refine-categories refine-grid"})
#print(container)

#subcontainer = container.find_all("div", {"class": "refine_items"})
brands = container.find_all('a',href=True)
#print(brands)
brandNames = container.find_all("span", {"class":"links-text"})
#print(brandNames)
aigo = "aigo"
asus = "asus"
brandurl = ""
#for brandName in brandNames:
    #print(str(brandName.get_text()))
for (brandName, brand) in zip(brandNames, brands):

    if str(brandName.get_text()).lower() == asus:
        brandurl = brand['href']

print(brandurl)




