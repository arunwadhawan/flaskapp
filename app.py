from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/piyush')
def piyush():
    return "hello Piyush"

@app.route('/ridhi')
def ridhi():
    return "hello Ridhi"

if __name__ == '__main__':
    app.run(debug=True)


	
