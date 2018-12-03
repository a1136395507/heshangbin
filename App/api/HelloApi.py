from flask_restful import Resource


class helloResource(Resource):
    def get(self):
        return 'hello flask'