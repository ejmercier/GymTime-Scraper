import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
URL = "http://connect2concepts.com/connect2/?type=circle&key=8E2C21D2-6F5D-45C1-AF9E-C23AEBFDA68B"

page = requests.get(URL, headers=headers)


soup = BeautifulSoup(page.content, "html.parser")

print(soup.prettify())
# filename = 'html.txt'
# f = open(filename, 'w')

# f.write(str(page))

count_items = soup.find_all('div', class_="col-md-3 col-sm-6")

df = pd.DataFrame(columns=["Name", "Date", "Time", "Count"])

for count in count_items:
    text = count.get_text()
    name = text.split('L')[0]
    temp = text.split('L')[1]

    time = temp.split(' ')[4] + ' ' + temp.split(' ')[5]
    date = temp.split(':')[2]
    date = date.split(' ')[1]

    count = temp.split(':')[1]
    count = count.split('U')[0]
    count = int(count)

    df = df.append({'Name' : name, 'Date' : date, 'Time' : time, 'Count' : count}, ignore_index = True)
    

    # print(name + " " + date + " " + time + " " + str(count))
df