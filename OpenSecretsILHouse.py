import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
path = "https://www.opensecrets.org/races/election?id=IL"
response = http.request('GET', path)
soup = BeautifulSoup(response.data, "html.parser")
