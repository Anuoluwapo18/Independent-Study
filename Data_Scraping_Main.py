
from bs4 import BeautifulSoup
import requests

url = 'https://www.globaldata.com/data-insights/macroeconomic/literacy-rate-in-nigeria/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Example: Extract table data
table_data = soup.find_all('table')