from enum import Enum
import logging
import yaml


class IODir(Enum):
    r = 'readonly'
    w = 'writeonly'
    rw = 'rw'


class Reset(Enum):
    no = 'no'
    auto = 'auto'


class Mask:
    def __init__(self, bit, label, reset=Reset.no, info=""):
        self.bit = bit
        self.label = label
        self.mask = 1 << bit
        self.info = info
        self.reset = reset

    def __call__(self, register):
        return (register & self.mask) == self.mask

    @staticmethod
    def factory(bit, label, info="", reset=Reset.no, **kwargs):
        bit = int(bit)
        reset = reset if isinstance(reset, Reset) else Reset[reset]
        if kwargs:
            logging.warning('Mask: Unexpected kwargs %s', kwargs.keys())

        return Mask(bit=bit, label=label, info=info, reset=reset)

    def __str__(self):
        return yaml.dump([self])


class Address:
    def __init__(self, page, offset, width=4, io=IODir.r):
        self.page = page
        self.width = width
        self.offset = offset
        self.io = io

    @staticmethod
    def factory(page, offset, width=4, io=IODir.r, **kwargs):
        page = int(page)
        width = int(width)
        offset = int(offset)
        io = IODir[io]
        if kwargs:
            logging.warning('Address: Unexpected kwargs %s', kwargs.keys())
        return Address(page=page, width=width, offset=offset, io=io)

    def __str__(self):
        return yaml.dump([self])


class Register:
    def __init__(self, address, masks=None, info="", value=None, default_value=None):
        self.address = address
        self.masks = masks or []
        self.info = info
        self.value = value
        self.default_value = default_value

    def get_active_label(self, state):
        return [mask.label for mask in self.masks if mask(state)]

    @staticmethod
    def factory(address, masks=None, info="",value=None, default_value=None, **kwargs):
        address = address if isinstance(address, Address) else Address.factory(**address)

        masks = masks or {}
        masks = [m if isinstance(m, Mask) else Mask.factory(bit, **m) for bit, m in masks.items()]
        if kwargs:
            logging.warning('Register: Unexpected kwargs %s', kwargs.keys())
        return Register(address=address, masks=masks, info=info, value=value, default_value=default_value)

    def __str__(self):
        return yaml.dump([self])


class Fifo:
    def __init__(self, address, depth, info=""):
        self.address = address
        self.depth = depth
        self.info = info

    @staticmethod
    def factory(address, depth, info="", **kwargs):
        address = address if isinstance(address, Address) else Address.factory(**address)
        if kwargs:
            logging.warning('Fifo: Unexpected kwargs %s', kwargs.keys())
        return Fifo(address=address, depth=depth, info=info, **kwargs)

    def __str__(self):
        return yaml.dump([self])
