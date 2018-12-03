from flask_restful import Api

from App.api.CheckenameApi import checkeResource
from App.api.GoodsApi import GoodsResource
from App.api.HelloApi import helloResource
from App.api.RegisterApi import RegisterResource
from App.api.WheelApi import WheelResource

api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(helloResource,'/hello/')
api.add_resource(WheelResource,'/wheel/')
api.add_resource(GoodsResource,'/goods/')
api.add_resource(checkeResource,'/checkuser/')
# api.add_resource(RegisterResource,'/register/')