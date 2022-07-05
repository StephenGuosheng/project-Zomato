
import pandas as pd
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

url = 'https://www.zomato.com/istanbul/dine-out'
chrome_options = Options()
chrome_options.add_argument("--lang=en-US")

driver = webdriver.Chrome(options=chrome_options)
driver.get (url)

sleep(randint(1, 3))
previous_height = driver.execute_script('return document.body.scrollHeight')

while True:
  driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
  sleep(randint(1, 3))
  new_height = driver.execute_script('return document.body.scrollHeight')
  containers = driver.find_elements (By.CLASS_NAME, 'jumbo-tracker')
  if new_height == previous_height:
    break
  previous_height = new_height

contain_list = []

for container in containers:
  restaurant =  container.find_element (By.XPATH,' .//h4[1]').text
  rating = container. find_element (By.XPATH,' .//div/a[2]/div[1]/div/div/div/div/div/div[1]').text
  genre = container.find_element (By.XPATH,' . //div/a[2]/div[2]/p[1]').text
  price = container.find_element (By.XPATH,' . //div/a[2]/div[2]/p[2]').text
  address = container.find_element (By.XPATH,' . //div/a[2]/p[1]').text

  print (restaurant,rating)

  container_item = {
    'restaurant': restaurant,
    'rating':rating,
    'genre':genre,
    'price': price,
    'address':address}

  contain_list.append(container_item)

df = pd.DataFrame(contain_list)
# save dataframe to csv
print (df)
df.to_csv('istanbul_dining out.csv')
