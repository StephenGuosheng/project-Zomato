import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


url = 'https://www.zomato.com/grande-lisboa/collections'
chrome_options = Options()
chrome_options.add_argument("--lang=en-US")

driver = webdriver.Chrome(options=chrome_options)
driver.get (url)
# containers
containers = driver.find_elements(By.XPATH, ' .//div[@id="root"]/div[2]/div[3]/div/section[2]/section/div/div')

contain_list = []

for container in containers:
    theme  = container.find_element(By.XPATH, ' .//section/a/section/section/p').text

    num = container.find_element(By.XPATH, ' .//section/a/section/section/div/h6').text
    print(theme, num)
    container_item = {
        'theme': theme,
        'number of places': num}

    contain_list.append(container_item)

df = pd.DataFrame(contain_list)
# save dataframe to csv
print (df)
df.to_csv('Lisbon collection.csv')