#!/usr/bin/env python3

import os
from flask import Flask, render_template

app = Flask(__name__)

... 
...

color = os.environ.get('APP_COLOR')

@app.route("/")
def main():
    color = {
        'blue': '002aff',
        'yellow': 'e1eb34',
        'green': '28fc03',
        'red': 'fc1703', 
        'purple': 'b503fc'
    }

    print(color)
    return render_template('hello.html', color=color)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")