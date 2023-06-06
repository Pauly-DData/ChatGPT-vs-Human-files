from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

s=Service(r"C:/Users/1948NM/Documents/Information Management/Thesis/Code/chromedriver.exe")
website = 'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Cleaning%20Data%20in%20Python/Instructions/Chapter%202%20-%20Tidying%20data%20for%20analysis.md#reshaping-your-data-using-melt'
driver = webdriver.Chrome(service=s)
driver.get(website)

questions = driver.find_elements(By.TAG_NAME, value = 'p')


for question in questions:
    
    print(question.text)
    
driver.quit()    




        







