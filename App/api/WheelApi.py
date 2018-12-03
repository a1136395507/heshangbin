
from flask_restful import Resource, fields,marshal_with
from App.models import Wheel

#
wheel_fileds = {
    'img':fields.String,
    'name':fields.String,
}

result_fields={
    'statuts':fields.Integer,
    'msg':fields.String,
    'data':fields.List(fields.Nested(wheel_fileds))
}

class WheelResource(Resource):
    @marshal_with(result_fields)
    def get(self):

        # 传递数据到页面
        wheels =Wheel.query.all()
        # print(wheels)
        response_data = {
            'statuts':200,
            'msg':'获取图片成功',
            'data':wheels
        }
        return response_data