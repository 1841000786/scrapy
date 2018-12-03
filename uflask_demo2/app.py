#路由详解
from flask import Flask,render_template,url_for

app=Flask(__name__)

# 固定路由          127.0.0.1
@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/service')  # 127.0.0.1:5000/service
def service():
    print(url_for('service'))
    return '服务业面'
@app.route('/about')
def about():
    return '关于我们'

# 带参数的路由.优点可以写多个参数
# http://www.xxx.com/product_list?pageno=1


@app.route('/product_list/<int:page_no>')
@app.route('/prodect_list',defaults={'page_no:1'})
def product_list(page_no):
    print(page_no,type(page_no))
    # page_no=int(page_no)
    return '商品1，商品2...'

if __name__=='__main__':
    # app.run(debug=True,host='0.0.0.0',port=50001)
    # app.run(debug=True,host='127.0.0.1',port='5001')
    app.run(port=5000)

"""

路由
1、匹配固定地址
'/'→'//127.0.0.1:5000/      //127.0.0.1:5000匹配更目录

flask命令行工具
flask run--port=5000 --host='0.0.0.0'

url_for(endpoint) 函数，构造url：
endpoint端点参数，填写方法名。注意参数对应的是函数名，跟路由的url没关系。
1. 当ip、port发生变化时，不用前端页面。
2. 引用css js之类的静态资源。flask框架会对url进行预处理，前端html页面引用资源时不能写成相对路径。前端url_for()返回结果/static/index。css，flask框架内置相关路由。


匹配可变url:
@app.route('/prodect_list/<int:page_no>')
[domain]/prodect_list
常见错误
1. templates notfound 模板未找到，检查.html文件的位置

"""
