from flask import Flask,render_template,url_for
from forms import Login


app = Flask(__name__)
app.config['SECRET_KEY'] = 'skljba223'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login',methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        pass
    return render_template('login.html',form=form)



if __name__ == '__main__':
    app.run()
