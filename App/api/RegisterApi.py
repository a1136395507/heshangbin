import time
import uuid


from flask_restful import Resource,reqparse,fields,marshal_with


# 请求格式定制
from werkzeug.security import generate_password_hash

from App.ext import db
from App.models import User

# 请求 格式定制
parser = reqparse.RequestParser()
parser.add_argument('username',type=str,required = True,help='请输入用户名')
parser.add_argument('password',type=str,required = True,help='请输入密码')
# parser.add_argument('icon', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='请选择图片')



# 响应 格式定制
# 定义函

user_fields = {
    'username': fields.String,
    'password':fields.String,
    'token': fields.String,
}

# 格式定制
result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'error':fields.String(default=''),
    'date': fields.String,
    'data': fields.Nested(user_fields, default='') # 默认是空
}


class RegisterResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        # 返回数据
        response_data = {
            'status': 406,
            'msg': '注册失败',
            'date': str(time.ctime())
        }
        # 获取 所有列表数据
        parse =parser.parse_args()
        # 实例化user
        user = User()
        # 用户名
        user.username = parse.get('username')
        # 密码
        user.password = generate_password_hash(parse.get('password'))

        # 状态保持
        user.token=str(uuid.uuid5(uuid.uuid4(),'register'))


        # 保存到数据库
        db.session.add(user)
        db.session.commit()

        # 返回数据
        response_data['status'] = 200
        response_data['msg'] = '注册成功'
        response_data['data'] = user

        return response_data

