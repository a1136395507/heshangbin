from flask_restful import Resource, fields ,marshal_with


# 格式定制
from App.models import Goods

wheel_fileds = {
    'img':fields.String,
    'name':fields.String,
    'price':fields.String,
}

result_fields={
    'statuts':fields.Integer,
    'msg':fields.String,
    'data':fields.List(fields.Nested(wheel_fileds))
}

class GoodsResource(Resource):
    @marshal_with(result_fields)
    def get(self):
        # 获取商品列表

        goodslis = Goods.query.all()
        # print(goodslist)
        response_data = {
            'statuts':200,
            'msg':'获取数据成功',
            'data':goodslis

        }

        return response_data

