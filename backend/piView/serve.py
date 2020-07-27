from flask import Flask, request
from flask_restful import Resource, Api

from piView.loader import Loader, JSONEncoder, example

block = Loader.load(example)

app = Flask("piView.serve")
api = Api(app)
app.config['RESTFUL_JSON'] = {'cls':JSONEncoder}

blocks = dict(main=block)


class Blocks(Resource):

    def get(self, name=None):
        if name is None:
            return blocks

        block = blocks.get(name)
        return {name: block}


api.add_resource(Blocks, '/block/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)