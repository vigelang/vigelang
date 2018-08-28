from flask import Flask
from json_format import device_class

app = Flask(__name__)

@app.route('/<ip_1>/info')
def hello_world(ip_1):
    a=device_class(ip_1,'22611')
    return str(a)

if __name__ == '__main__':
   app.run('0.0.0.0',port='8000')
