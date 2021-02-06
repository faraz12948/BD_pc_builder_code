from bs4 import BeautifulSoup
import requests



base_url = 'https://www.techlandbd.com/pc-components'



result = requests.get(base_url)
src = result.content
soup = BeautifulSoup( src , 'lxml')



product_list = soup.find_all("div", {"class": "product-thumb"})
#print(product_list)
product_info = []

for product in product_list:
        product_title = product.find(class_='name').text
        product_url = product.find('a',href=True).get('href')
    
    

        if product.find(class_='price-normal'):
              product_price = product.find(class_='price-normal').text
            
        else:
              product_price = 'N/A'

        if product.find(class_='image'):
              product_image_url = product.find('img').get('src')
       

        product_info.append((product_title, product_url,product_price,product_image_url))


print(product_info)



