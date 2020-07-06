from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

registers = dict()

class Registers(Resource):

    def get(self, name):
        return {name: registers[name]}

    def put(self, name):
        registers[name] = request.form['data']
        return {name: registers[name]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)