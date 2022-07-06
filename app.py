from flask import Flask
app = Flask(__name__)

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    content = request.get_json()
    print (content)
    return 'JSON posted'

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=0)
