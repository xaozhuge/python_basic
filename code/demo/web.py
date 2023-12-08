from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/route1')
def route1():
    return 'This is route 1'

# 第二个路由
@app.route('/route2')
def route2():
    return 'This is route 2'

# 通用路由处理函数
# @app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return f'This is a catch-all route. Path: {path}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

'''
docker exec python380_c python3 demo/web.py
'''