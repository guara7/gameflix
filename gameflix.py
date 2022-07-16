from flask import Flask

app = Flask(__name__)

@app.route('/home')
def ola():
    return '<h2>ola mundo</h2>'

app.run()
