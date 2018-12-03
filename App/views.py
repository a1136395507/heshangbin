import uuid

from flask import Blueprint, request, session, redirect, url_for, send_file, render_template
from flask.json import jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db

from App.models import User

blue = Blueprint('blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)


# 首页
@blue.route('/index/')
def index():
    token = session.get('token')
    if token:
        # 获取到用户名
        user = User.query.filter(User.token == token).first()
        return render_template('index.html', user=user)

        # 跳转到静态页面
        # return send_file("static/html/home_logined.html")

    else:

        return render_template('index.html')






@blue.route('/register/', methods=['POST','GET'])
def register():
    if request.method  =="POST":
        username = request.form.get('username')
        password = request.form.get('password')

        # 存入数据库
        user = User()
        user.username = username
        user.password = generate_password_hash(password)
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        db.session.add(user)
        db.session.commit()

        # 状态保持
        session['token'] = user.token

        return redirect(url_for('blue.index'))
    elif request.method =="GET":

        return render_template('register.html')


@blue.route('/login/',methods=["POST","GET"])
def login():
    if request.method =="POST":
        # 获取用户名密码
        username = request.form.get('username')
        password =request.form.get('password')


        users = User.query.filter(User.username==username)
        user = users.first()
        if users.count():
            if check_password_hash(user.password, password):


            # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                db.session.add(user)
                db.session.commit()


            # 状态保存
                session['token']=user.token
            return redirect(url_for('blue.index'))
        else:
            return '用户名或者密码错误'

    elif request.method == "GET":

        return render_template('login.html')


@blue.route('/logout/')
def logout():
    session.pop('token')
    return redirect(url_for('blue.index'))
