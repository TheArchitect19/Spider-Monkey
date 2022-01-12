from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests


def home(request):
    return render(request, 'scrapper.html')


def flipkart_elec(key, mainData):
    def url(query):
        url = "https://www.flipkart.com/search?q=" + \
            query.replace(
                ' ', '%20')+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return url
    url = url(key)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('a', class_="_1fQZEK")

    for i in lists:
        title = i.find('div', class_="_4rR01T").text
        price = i.find('div', class_="_30jeq3 _1_WHN1").text
        image = i.find('img')
        if (i != '#'):
            all_links = "https://www.flipkart.com"+i.get('href')
        mainData[title] = [price, all_links]
    return mainData


def flipkart(key, mainData):
    def url_generator(query):
        url = "https://www.flipkart.com/search?q=" + \
            query.replace(
                ' ', '%20')+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return url
    url = url_generator(key)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('div', class_="_1xHGtK _373qXS")
    data = {}
    for i in lists:
        title = i.find('a', class_="IRpwTa").text
        price = i.find('div', class_="_30jeq3").text
        link = i.find('a', class_="_2UzuFa").get('href')
        link = "https://www.flipkart.com" + link
        mainData[title] = [price, link]
    return mainData


def snapdeal(key, mainData):
    def url(query):
        url = "https://www.snapdeal.com/search?keyword=" + \
            query.replace(' ', '%20')+"&santizedKeyword=shoes&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy"
        return url
    url = url(key)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('div', class_="product-tuple-description")
    if soup.find('span', class_="nnn").text == "Sorry, we've got no results for 'puma shoes'":
        return mainData
    else:
        for i in lists:
            title = i.find('p', class_="product-title").text
            price = i.find('span', class_="lfloat product-price").text
            link = i.find('a', class_="dp-widget-link noUdLine").get('href')
            mainData[title] = [price, link]
        return mainData


def bewakoof(key, mainData):
    def url(query):
        url = "https://www.bewakoof.com/search/" + \
            query.replace(' ', '%20')+"?ga_q="+query.replace(' ', '%20')
        return url
    url = url(key)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('a', class_="col-sm-4 col-xs-6")
    for i in lists:
        try:
            title = i.find('h3', id=True).text
            price = i.find('b').text
            image = i.find('div', class_="productImg").img
            all_links = ""
            if (i != '#'):
                all_links += "https://www.bewakoof.com"+i.get('href')
            mainData[title] = [price, all_links]
        except:
            return mainData
    return mainData


def search(request):
    d = request.POST
    term = d['text']
    print(term)
    mainData = {}
    mainData = flipkart(term, mainData)
    mainData = flipkart_elec(term, mainData)
    mainData = snapdeal(term, mainData)
    mainData = bewakoof(term, mainData)
    context = {'data': mainData}
    return render(request, "results.html", context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
