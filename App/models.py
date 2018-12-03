from App.ext import db


class Wheel(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(40))

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 图片
    img = db.Column(db.String(200))
    # 名称
    name = db.Column(db.String(50))
    # 价格
    price = db.Column(db.String(50))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 用户名 手机/邮箱
    username = db.Column(db.String(40),nullable=True)
    password = db.Column(db.String(256))
    token = db.Column(db.String(256))
