from flask import Flask, template_rendered, render_template
from dotenv import load_dotenv
import datetime
import random

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
  random_number = random.randint(1,10)
  year = datetime.date.today().year
  print(year)
  return render_template('index.html', num = random_number, year=year)

if(__name__ == '__main__'):
  app.run(debug=True, port=8000)