#!/usr/bin/python3
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        data = request.form.get('data')
        with open('/data/data.txt', 'w') as f:
            f.write(data)
    else:
        if os.path.exists('/data/data.txt'):
            with open('/data/data.txt', 'r') as f:
                data = f.read()
    if data:
        return render_template('index.html', data=data)
    else:
        return render_template('index.html', data='<null>')

if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')
