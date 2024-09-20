from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy

url = 'https://fragrancebuy.ca/collections/fullproductcatalogue'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')