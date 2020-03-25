from pymongo import MongoClient
import requests
from pprint import pprint
from lxml import html

client = MongoClient('localhost', 27017)
db = client['STV_data']
tc_tv = db.tc_stv_data
tk_tv = db.tk_stv_data


main_link_tc = 'https://www.tricolor.tv/channelpackages/?source=header&section=services&menu=packages-and-services'
response_tc = requests.get(main_link_tc).text
tree_tc = html.fromstring(response_tc)
packages_tc = tree_tc.xpath("//div[@class='list-item']")

for package_tc in packages_tc:

    name = package_tc.xpath("./a[@class='list-item-link']/div[@class='item-title']/div[@class='title-label']/text()")
    link = package_tc.xpath("./a[@class='list-item-link']/@href")
    description = package_tc.xpath("./a[@class='list-item-link']/div[@class='item-text']/p/text()")
    price = package_tc.xpath("./a[@class='list-item-link']/ul[@class='item-info']/li/text()")[0:2]

    packages_tc_info = zip( name, link, description, price)
    for name, link, description, price in packages_tc_info:
        duplicates = tc_tv.find_one({'name': name, 'link': link, 'description': description, 'price': price})
        if duplicates == None:
            tc_tv.insert_one({'name': name, 'link': link, 'description': description, 'price': price})
        else:
            pass

main_link_tk = 'https://www.telekarta.tv/packages/'
response_tk = requests.get(main_link_tk).text
tree_tk = html.fromstring(response_tk)
packages_tk = tree_tk.xpath("//div[@id='tariffs']")

for package_tk in packages_tk:

    name = package_tk.xpath(".//a/div/h3/text()")
    description= package_tk.xpath(".//div[@class='tabs-accordion__option-inner']//span[@class='package-selection__channels-number'][1]/text()")
    price = package_tk.xpath(".//div[@class='package-selection__price-value'][1]/span[@class='number number--md']/text()")
    price2 = package_tk.xpath(".//div[@class='package-selection__price-value'][2]/span[@class='number number--md']/text()")
    packages_tk_info = zip( name, description, price, price2)
    for name,  description, price, price2 in packages_tk_info:
        duplicates = tk_tv.find_one({'name': name, 'description': description, 'price': price,'price2': price2})
        if duplicates == None:
            tk_tv.insert_one({'name': name, 'description': description, 'price': price,'price2': price2 })
        else:
            pass

for price in tc_tv.find({'price':{'$gt': '1500'}}):
    pprint(price)