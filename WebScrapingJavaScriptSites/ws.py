#!/usr/bin
from bs4 import BeautifulSoup as soup
import requests
import os
import shutil
import time
from selenium import webdriver
url = 'https://www.wayfair.com/furniture/sb0/sofas-c413892.html'
web_r=requests.get(url)
web_soup = soup(web_r.text, "html.parser")

driver = webdriver.Firefox()
driver.get('https://www.google.com/search?rlz=1C5CHFA_enUS772US773&biw=1224&bih=598&tbm=isch&sa=1&ei=HV_5XO2pMM2f_QbP64TwAQ&q=sectional+sofa&oq=sectional+sofa&gs_l=img.3..0l10.2405.4954..5235...0.0..0.98.992.14......0....1..gws-wiz-img.......35i39j0i67.6NSpN2K5q60')

itt = 0
while itt <10:
    html = driver.execute_script("return document.documentElement.outerHTML")
    sel_soup =soup(html, "html.parser")
    images = []
    images_list = sel_soup.findAll('img')
    for im in images_list:
        src = im["src"]
        images.append(src)
    current_path = os.getcwd()
    for img in images:
        try:
            file_name = os.path.basename(img)
            img_r = requests.get(img, stream=True)
            new_path = os.path.join(current_path, "images",file_name)
            with open(new_path,"wb") as output_file:
                shutil.copyfileobj(img_r.raw,output_file)
            del img_r
        except:
            pass
    itt += 1
    time.sleep(5)




'''
images =[]
images = web_soup.findAll('img')
print(len(images))
for image in images:
    print(image.get('src'))

page_soup=soup(page_html, "html.parser")
print(page_soup.h1)
print(page_soup.body.span)
containers =page_soup.findAll("div",{"class":"ProductDetailImageCarouselVariantB-image"})
print(len(containers))
contain = containers[0]
print(contain.div.div.img["src"])
'''
