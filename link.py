import requests
from bs4 import BeautifulSoup



a = requests.get("https://www.w3schools.com/python/python_file_open.asp")
soup = BeautifulSoup(a.content, 'html.parser')
print(soup.get_text().split()[100])
