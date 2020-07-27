import os
import argparse
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

from piView.loader import Loader, JSONEncoder, example


app = Flask("piView.serve")
api = Api(app)

app.config['RESTFUL_JSON'] = {'cls':JSONEncoder}
CORS(app)

blocks = dict()


class Blocks(Resource):

    def get(self, ):
        return blocks


class Block(Resource):

    def get(self, name=None):
        assert name in blocks

        block = blocks.get(name)
        return {name: block}


api.add_resource(Block, '/block/<string:name>')
api.add_resource(Blocks, '/block/')


def get_parser(parser=None):
    parser = argparse.ArgumentParser() if parser is None else parser
    parser.add_argument('config', nargs='?', default=example)
    parser.add_argument('-debug', action='store_true')
    return parser


def run(debug=True, config=example):
    assert os.path.exists(config), "Missing Config file"
    block = Loader.load(config)
    blocks[block.name] = block

    return app.run(debug=debug)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    run(debug=args.debug, config=args.config)
