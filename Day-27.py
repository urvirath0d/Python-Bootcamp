import requests
import bs4
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text,'html.parser')

cases = soup.find_all('div' ,class_= 'maincounter-number')

data = []

for i in cases:
    span = i.find('span')
    data.append(span.string)

print(data)

df = pd.DataFrame({"CoronaData": data})

df.index = ['TotalCases', ' Deaths', 'Recovered']

df.to_excel('Vaccine.xlsx')