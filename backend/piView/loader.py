import yaml
from piView.register import Register, Mask, Fifo
from piView.layout import Block

class Loader:

    @staticmethod
    def load(filename):
        handle = open(filename, 'r')
        parsed_file = yaml.load(handle, Loader=yaml.FullLoader)

        return Block.factory(**parsed_file)


if __name__ == '__main__':
    print(Loader.load('example/config.yml'))