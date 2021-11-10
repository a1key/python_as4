import requests
from flask import Flask, app,render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)
r = requests.get('https://coinmarketcap.com/ru/currencies/bitcoin/')

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'Post':
        check = request.form['check']
    return render_template('test.php')
if __name__ == '__main__':
    app.run(debug=True)
