# Flights Schedule scrap from Airport site

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

url = "http://www.klia.com.my/index.php?m=airport&c=flight_schedule"

uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

#container = page_soup.find("div", {'class': 'tab-list-wrap02'})

contain =page_soup.findAll('tr')

klia =[]
for table in contain:
      klia.append(table.get_text()+ ',')

klia1 =[]
for i in klia:
    tmp = i.replace('\n',',')
    klia1.append(tmp[1:-1])

df = pd.DataFrame(klia1)

df.to_csv('flight.csv', mode='w',index=False)
