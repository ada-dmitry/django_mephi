from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = Service('D:\\teach\Prog\chromedriver.exe')
browser = webdriver.Chrome(service=driver)
browser.get(
    'https://amwine.ru/catalog/igristoe_vino_i_shampanskoe/igristoe_vino/')
html_code = browser.page_source
b_soup = BeautifulSoup(html_code, 'lxml')
name = b_soup.find_all(
    'a', class_="catalog-list-item__title js-product-detail-link")
price = b_soup.find_all('span', class_="middle_price")
priceDis = b_soup.find_all('span', class_="baseoldprice")
mark = b_soup.find_all('span', class_="product-rating__rating")
pictures = b_soup.find_all('div', class_="catalog-list-item__img-wrapper")
