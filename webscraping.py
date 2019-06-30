from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from pandas import DataFrame

url = 'https://www.sfu.ca/computing/people/faculty.html'
client = urlopen(url)
raw_html = client.read()
client.close()

page_details = BeautifulSoup(raw_html,"html.parser")
grabProfessors = page_details.findAll("div",{"class":"half"})

titlel = []
bodyl = []
# print(grabProfessors[0])
for proff in grabProfessors:
    title = str(proff.h4)
    body = str(proff.p)
    body = re.sub('<.*?>', '', body).lstrip('Area:').rstrip('\n')
    titlel.append(re.sub('<.*?>', '', title))
    bodyl.append(body)
df = DataFrame({'Name & Desig. ':titlel,
                'Area of Interest':bodyl}
               )
df.to_csv('facultyList.csv',index=False)
print("Done...")
