'''
https://www.youtube.com/watch?v=Z1RJmh_OqeA
Learn Flask for Python - Full Tutorial
Day 1
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True)