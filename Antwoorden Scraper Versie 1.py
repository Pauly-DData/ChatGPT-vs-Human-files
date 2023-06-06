from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

# create a list of URLs to scrape
urls = [
        
       'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Chapter%201%20-%20Introduction%20and%20flat%20files.py',
       'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Chapter%202%20-%20Importing%20data%20from%20other%20file%20types.py',
       'https://github.com/AmoDinho/datacamp-python-data-science-track/blob/master/Importing%20Data%20in%20Python%20pt1/Chapter%203%20-%20Working%20with%20relational%20databases%20in%20Python.py'
]

s = Service(r"C:\Users\1948NM\Documents\Information Management\Thesis\Code\chromedriver_win32.zip\chromedriver.exe")

# create an empty dataframe to store the scraped data
df = pd.DataFrame(columns=['answer'])

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)

    questions = driver.find_elements(By.TAG_NAME, value='td')

    for answer in questions:
        # store the text content of each element in the dataframe
        df.loc[len(df.index)] = {'answer': answer.text}

    driver.quit()

# Remove rows that contain only whitespace
df = df[df['answer'].str.strip().astype(bool)]

# export the dataframe to a CSV file
df.to_csv('AntwoordenVanuitGitHub_importing_data_in_python_part_1.csv', index=False)
