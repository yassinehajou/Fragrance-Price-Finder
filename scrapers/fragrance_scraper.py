from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlalchemy

website = 'https://fragrancebuy.ca/collections/fullproductcatalogue'
response = requests.get(website)

soup = BeautifulSoup()