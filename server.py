from flask import Flask, template_rendered, render_template
from dotenv import load_dotenv
import random

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
  random_number = random.randint(1,10)
  return render_template('index.html', num = random_number)

if(__name__ == '__main__'):
  app.run(debug=True, port=8000)