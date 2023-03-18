from flask import Flask, template_rendered, render_template
from dotenv import load_dotenv
import datetime
import random
import requests

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
  random_number = random.randint(1,10)
  year = datetime.date.today().year
  print(year)
  return render_template('index.html', num = random_number, year=year)

@app.route('/guess/<name>')
def guess_name(name):
  response = requests.get(f'https://api.genderize.io?name={name}')
  response.raise_for_status()
  data = response.json()
  return render_template('guess.html', data=data)


if(__name__ == '__main__'):
  app.run(debug=True, port=8000)