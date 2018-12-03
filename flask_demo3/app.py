# post请求    request上下文context   响应response

from flask import Flask,render_template,url_for,request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'
# 传参数的url
# http://127.0.0.1:5000/prodect_list?page_no=1&cat=sport
@app.route('/prodect_list')
def prodect_list():
    args = request.args
    print(args)
    print(args['page_no'])
    print(args['cat'])
# 数据库查询pass
    return '商品1，商品2...'

@app.route('/login')
def login():
    print(request)
    return render_template('login.html')

@app.route('/login_submit',methods=['POST'])
def login_submit():
    form = request.form
    print(format)
    username = form['username']
    password = form['password']
    print(username,password)
    return '表单提交完成'


if __name__ == '__main__':
    app.run()



""" 
request:flask框架中全局变量，存储着跟着请求相关信息。


"""