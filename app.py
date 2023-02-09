import json
from flask import Flask, jsonify, render_template

import requests

from bs4 import BeautifulSoup

# URL to fetch data from
url = "https://moneycontrol.com/"

#commodity class
class commodity:
    def __init__(self,name,price,change,per_change):
        self.name = name
        self.price = price
        self.change = change
        self.per_change = per_change



# function to get values from moneycontrol website
def getItems():
    r = requests.get(url)

    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')



    div = soup.find('div', attrs={'class':'PR tab-pane in active fade'})

    table = div.find('table',attrs={'class': 'rhsglTbl'})
    rows = table.find_all('tr')

    i = 0

    como = []
    for row in rows:

        if i == 0:
            i+=1
            continue
        else:
            # print(row)
            data = row.find_all('td')
            c = commodity(data[0].text.strip(),data[1].text.strip(),data[3].text.strip(),data[4].text.strip())
            como.append(c)
    
    return como



app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return render_template('index.html',como = getItems())

    


if __name__ == "__main__":
    app.run(debug=True)