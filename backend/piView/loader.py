import os
import yaml
from piView.register import Register, Mask, Fifo, IODir, Reset
from piView.layout import Block
from flask.json import JSONEncoder as FlaskJSONEncoder

example = os.path.dirname(__file__)
example = os.path.join(example, '../../example/config.yml')
example = os.path.abspath(example)


class Loader:

    @staticmethod
    def load(filename):
        handle = open(filename, 'r')
        parsed_file = yaml.load(handle, Loader=yaml.FullLoader)

        return Block.factory(**parsed_file)


custom_types = (Block, Mask, Register, Fifo)
enum_types = (IODir, Reset)
json_types = (float, int, str, dict, list)
all_types = custom_types + json_types + enum_types


class JSONEncoder(FlaskJSONEncoder):

    def default(self, o):
        if isinstance(o, custom_types):
            data = dict()
            keys = [_ for _ in dir(o) if not _.startswith('_')]
            for key in keys:
                value = getattr(o, key)
                if not isinstance(value, all_types):
                    continue

                data[key] = value

            return data
        elif isinstance(o, enum_types):
            return str(o.name)

        return FlaskJSONEncoder.default(self, o)


if __name__ == '__main__':
    print(Loader.load('example/config.yml'))