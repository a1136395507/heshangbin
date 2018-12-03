import time

from flask_restful import marshal_with, Resource, fields, reqparse

from App.models import User

parser =reqparse.RequestParser()
parser.add_argument('username',type=str,required = True,help='请输入用户名')



class checkeResource(Resource):
    def get(self):
        parse = parser.parse_args()

        # 判断用户名是否重复
        users = User.query.filter(User.username == parse.get('username'))

        if users.count() > 0:  # 用户名存在
            response_data={
                            'status' : 401,
                            'error' : '用户名已存在'
                           }
            return response_data
        else:                   # 用户名不存在
            response_data = {
                        'status': 200,
                        'error': '用户可用'
                             }
            return response_data



