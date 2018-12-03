from flask import Flask

from App.api import init_api
from App.ext import init_ext
from App.settings import init_cogfig
from App.views import init_blue


def create_app(env_name=None):

    app = Flask(__name__)


    # 配置config
    init_cogfig(app,env_name)


    # 扩展ext
    init_ext(app)

    # api
    init_api(app)

    # 蓝图
    init_blue(app)


    return app