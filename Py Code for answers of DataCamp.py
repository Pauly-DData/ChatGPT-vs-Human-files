from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# create a list of URLs to scrape
urls = [
    'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Chapter%201%20-Exploring%20your%20data.py'
    ]

s = Service(r"C:/Users/1948NM/Documents/Information Management/Thesis/Code/chromedriver.exe")

# create an empty dataframe to store the scraped data
df = pd.DataFrame(columns=['code'])

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    # find all p elements on the page
    p_elements = driver.find_elements(By.TAG_NAME, value='td')

    # iterate over every other p element starting from the second one
    for i in range(1, len(p_elements), 2):
        # store the text content of the p element in the dataframe
        df = df.append({'code': p_elements[i].text}, ignore_index=True)

    driver.quit()
    

# export the dataframe to a CSV file
df.to_csv('outputCODE.csv', index=False)

# read the csv file into a pandas dataframe
df = pd.read_csv('outputCODE.csv')

# drop rows with all blank values
df.dropna(how='all', inplace=True)

# write the updated dataframe to a new csv file
df.to_csv('outputCODE.csv', index=False)

