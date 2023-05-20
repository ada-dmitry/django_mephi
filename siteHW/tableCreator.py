import psycopg2
import wget
import parser
import config


connection = psycopg2.connect(
    host=config.hostname, dbname=config.databname, user=config.username, password=config.passw)
cursor = connection.cursor()
creat_qwery = """ create table Parser 
    (id serial primary key, page_name varchar(100), price varchar(10), priceDis varchar(30), mark varchar(10), scr varchar(100))"""

try:
    cursor.execute(creat_qwery)
    connection.commit()
except psycopg2.errors.DuplicateTable:
    print("")


for i in range(15):
    url = 'https://amwine.ru' + \
          parser.pictures[i].find('a').find('img').attrs['data-src']
    filename = f"C:/Users/adadm/PycharmProjects/django_mephi/siteHW/polls/static/image/{i}.jpg"
    try:
        img = open(filename)
    except IOError as e:
        wget.download(url, filename)
    try:
        ins_qwery = f"""insert into public.Parser(page_name, price, priceDis, mark, scr) values ('{parser.name[i].text}', '{parser.price[i].text}', '{parser.priceDis[i].text}',  '{parser.mark[i].text}', '{filename}')"""
        cursor.execute(ins_qwery)
        connection.commit()
    except:
        connection.rollback()

cursor.close()
connection.close()
