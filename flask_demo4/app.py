import os
from flask import Flask,render_template,url_for,request,make_response,abort,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload_submit',methods =['POST'])
def upload_submit():
    file = request.files['file']
    print(file)
    # file.save('static/userfile/001.txt')  # 不建议写
    file.save('C:/Users/w1362/PycharmProjects/flask_demo4/static/userfile/001.txt')
    # os.path.dirname(__file__)  # app.py 所在的文件夹路径D:PycharmProjects\flask_demo4
    # sapve_path = os.path.dirname(__file__)+'/static/userfile'
    save_path = os.path.join(os.path.dirname(__file__),'static/userfile/',file.filename)
    print(save_path)
    file.save(save_path)
    return '保存完成'

@app.route('/login',methods=['GET','POST'])
def login():
    print(request.method)
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        print(username,password)
        # 数据库查询比对
        pass
    # 设置cookie
        response = make_response(render_template('index.html'))
        response.set_cookie('username',username,)
        return response
@app.route('/admin')
def admin():
    # 假设这个路由是管理后台，前来登录的用户权限验证失败
     abort(401)  #返回内置的错误模板页面

#如果想让错误的响应渲染一个更好看的模板
@app.errorhandler(404)
def error404(error):
    # return render_template('errorhandler.html'),404
    return redirect(url_for('hello_world'),code=302)

# 重定向redirect
# 场景：登陆成功了，进入我们的订单页面，登录失败，重定向到首页或登录页面让用户再次尝试登录，请求的路由发生变化


if __name__ == '__main__':
    app.run()

