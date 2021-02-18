from flask import Flask, render_template
import json
import os

app = Flask(__name__)

# Change direct to program's folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))

os.system('python fix.py')

with open("SixersFixed.json") as f:
   json_data = f.read()

sixers = json.loads(json_data)  # json loads method

@app.route('/')
@app.route('/About/')
def aboutPage():
   return render_template('about.html')

@app.route('/Sixers/')
def convertPage():
   return render_template('sixers.html', players=sixers)

if __name__ == "__main__":
   app.run()
