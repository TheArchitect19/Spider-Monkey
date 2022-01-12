from bs4 import BeautifulSoup
import requests
import csv

def flipkart(key):
    def url_generator(query):
        url="https://www.flipkart.com/search?q="+query.replace(' ','%20')+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return url
    url=url_generator(key)
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div', class_="_1xHGtK _373qXS")
    with open(f'{key}flipkart.csv','w',encoding= "utf8", newline="") as ps:
        thewriter=csv.writer(ps)
        header= ['Title' , 'Price']
        thewriter.writerow(header)
        for i in lists:
            title = i.find('a', class_= "IRpwTa").text
            price= i.find('div',class_="_30jeq3").text
            info=[title,price]
            thewriter.writerow(info)
    ps.close()

def flipkart_elec(key):
    def url(query):
        url="https://www.flipkart.com/search?q="+query.replace(' ','%20')+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return url
    url=url(key)
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('a', class_="_1fQZEK")
    with open(f'{key}flipkart.csv','w',encoding= "utf8", newline="") as ps:
        thewriter=csv.writer(ps)
        header= ['Title' , 'Price']
        thewriter.writerow(header)
        for i in lists:
            title = i.find('div', class_= "_4rR01T").text
            price= i.find('div',class_="_30jeq3 _1_WHN1").text
            info=[title,price]
            thewriter.writerow(info)
    ps.close()

def snapdeal(key):
    def url(query):
        url="https://www.snapdeal.com/search?keyword="+query.replace(' ','%20')+"&santizedKeyword=shoes&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy"
        return url
    url=url(key)
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div', class_="product-tuple-description")
    if soup.find('span', class_="nnn").text=="Sorry, we've got no results for 'puma shoes'":
        print("No results found for",f'{key}',"in snapdeal")
    else:
        with open(f'{key}_sd.csv','w',encoding= "utf8", newline="") as ps:
            thewriter=csv.writer(ps)
            header= ['Title' , 'Price']
            thewriter.writerow(header)
            for i in lists:
                title = i.find('p', class_= "product-title").text
                price= i.find('span',class_="lfloat product-price").text
                info=[title,price]
                thewriter.writerow(info)
        ps.close()

def paytmmall(key):
    def url(query):
        url="https://paytmmall.com/shop/search?q="+query.replace(' ','%20')+"&from=organic&child_site_id=6&site_id=2&category=5048%2C5254&brand=1447"
        return url
    url=url(key)
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div', class_="pCOS")
    with open(f'{key}_paytm.csv','w',encoding= "utf8", newline="") as ps:
        thewriter=csv.writer(ps)
        header= ['Title' , 'Price']
        thewriter.writerow(header)
        for i in lists:
            title = i.find('div', class_="UGUy").text
            price= i.find('div', class_="_1kMS").text
            info=[title,price]
            thewriter.writerow(info)
    ps.close()

    

key=input("Enter the name of product!\t")
num=int(input("Press 1. If it is a Electronic item.\nPress 2. If it is a clothing item.\n"))
if num==1:
    flipkart_elec(key)
elif num==2:
    flipkart(key)
snapdeal(key)
paytmmall(key)
print("Scrapping done successfully!")
