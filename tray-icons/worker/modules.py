from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import psycopg2
from selenium.webdriver.firefox.options import Options

con = psycopg2.connect(host="192.168.58.2",user='postgres',password='2908',database='postgres')
cur = con.cursor()

options = Options()
options.headless = True

def fun(name):
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.amazon.com')
    driver.find_element_by_id('twotabsearchtextbox').send_keys(name)
    driver.find_element_by_id('nav-search-submit-button').send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    pricewhole = driver.find_elements_by_class_name("a-price-whole")
    pricefraction = driver.find_elements_by_class_name("a-price-fraction")
    text = driver.find_elements_by_class_name("a-size-medium.a-color-base.a-text-normal")
    q = "insert into amazon (price,product_name) values (%s,%s)"
    t = ('$'+pricewhole[0].text+'.'+pricefraction[0].text,text[0].text)
    cur.execute(q,t)
    con.commit()
    print('inserted....')
    driver.quit()
    