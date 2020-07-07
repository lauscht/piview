import yaml
import logging
from piView.register import Register, Fifo


class Block:
    def __init__(self, name, info, version, registers=None, fifos=None):
        self.name = name
        self.info = info
        self.version = version

        self.fifos = fifos or dict()
        self.registers = registers or dict()

    @staticmethod
    def factory(name, info, version, fifos=None, registers=None, **kwargs):
        
        registers = registers or {}
        registers = dict((r, Register.factory(**v)) for r, v in registers.items())
        
        fifos = fifos or {}
        fifos = dict((f, Fifo.factory(**v)) for (f, v) in kwargs.pop('fifos', {}).items())
        if kwargs:
            logging.warning('Block: Unexpected kwargs %s', kwargs.keys())
        return Block(name, info, version, registers=registers, fifos=fifos)

    def __str__(self):
        return yaml.dump([self])