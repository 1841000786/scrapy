# # jinja2 前端模板渲染语法
# from flask import Flask,render_template, url_for,request, redirect
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#
#     name = '小李'
#     # 假设从数据库取得学生姓名列表
#     name_list = ['小明', '小红', '小青']
#     stu_list = [
#     {'name': '小明', 'age': 13, 'phone': '13700000'},
#     {'name': '小李', 'age': 13, 'phone': '13500000'},
#     {'name': '小请', 'age': 13, 'phone': '13600000'}
#     ]
#
#
#
#             # 假设从数据库取一个字段信息包含html语法
#     html_content="""
#     <body>
#         <h1>python</h1>
#     </body>
#     """
#     return render_template('index.html', name=name, name_list =name_list, stu_list=stu_list, html_content=html_content)
#
#
# @app.route('/adout')
# def adout():
#     return render_template('adout.html')
#
# if  __name__ == '__main__':
#     app.run()
# jinja2
# 前端模板渲染语法
from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    name = '小李'

    # 假设从数据库取的学生列表
    name_list = ['小明', '小红', '小青']
    stu_list = [
        {'name': '小明', 'age': 13, 'phone': '1375550'},
        {'name': '小红', 'age': 13, 'phone': '1235550'},
        {'name': '小青', 'age': 13, 'phone': '1465550'}
    ]

    # 假设从数据库中取出一个字段信息包含html语法
    html_content = """
            <body>
                <h1>python</h1>
            </body>

    """

    return render_template('index.html', name=name, name_list=name_list, stu_list=stu_list)


@app.route('/adout')
def adout():
    return render_template('adout.html')


if __name__ == '__main__':
    app.run()
