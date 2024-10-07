from bs4 import BeautifulSoup
from requests import session
import matplotlib.pyplot as plt

s = session()

header = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0','Accept':
'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
'sec-ch-ua-platform': 'Windows',
'set-cookie':'__ddg8_=O6NtpN2e2m5cQkTY; Domain=.mfd.ru; Path=/; Expires=Sun, 06-Oct-2024 12:48:02 GMT'
}

url = 'https://mfd.ru/currency/?currency=USD'
req = s.get(url, headers= header)

print(req)

soup = BeautifulSoup(req.content, 'lxml')

page1 = soup.find('table',class_="mfd-table mfd-currency-table").text.split()

for trash in page1:
	if trash == 'с':
		page1.remove(trash)
del page1[0:6]

page_data = page1[::3]
del page1[::3]
page_data.reverse()

page_course = page1[::2]
del page1[::2]
page_course.reverse()

page_change = page1[::]

x = []
y = []
for a in page_data[::8]:
	x.append(a)
#print(x)
for b in page_course[::8]:
	y.append(b)
#print(y)

plt.title('Доллар США')
plt.xlabel('Курс' , fontsize=12 , color= 'black')
plt.ylabel('Дата', fontsize=12 , color= 'black')
plt.plot(y,x)
plt.grid()
plt.show()



