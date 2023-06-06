from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r"C:/Users/1948NM/Documents/Information Management/Thesis/Code/chromedriver.exe")

driver = webdriver.Chrome(service=s)

url = 'https://github.com/AmoDinho/datacamp-python-data-science-track/tree/master/Unsupervised%20Learning%20in%20Python'

driver.get(url)

chapter_urls = []

while True:
    links = driver.find_elements(By.TAG_NAME, value='a')
    for link in links:
        url = link.get_attribute('href')
        if 'Chapter' in url:
            chapter_urls.append(url)
            print("'{}',".format(url))
    try:
        next_button = driver.find_element(By.XPATH, '//a[@rel="next"]')
        next_button.click()
    except:
        break

driver.quit()
