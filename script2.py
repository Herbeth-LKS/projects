import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#insert url

url = ""


driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get(url)

time.sleep(10)

driver.quit()

