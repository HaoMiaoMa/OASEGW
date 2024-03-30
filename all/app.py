from flask import Flask, render_template

app = Flask(__name__)

# 定义一个简单的路由，用于显示网站的主页
@app.route('/')
def index():
    return render_template('index.html')

# 如果您想添加更多的页面或功能，请在此处定义相应的路由

if __name__ == '__main__':
    app.run(debug=True)
