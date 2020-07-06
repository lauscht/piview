
class IODir(Enum):
    r = 'readonly'
    w = 'writeonly'
    rw = 'rw'


class Mask:
    def __init__(self, bit, label):
        self.bit = bit
        self.label = label
        self.mask = 1 << bit

    def __call__(self, register):
        return (register & mask) == self.mask


class Register:
    def __init__(self, page, offset, width=4, direction=IODir.r, masks=None, description=""):
        self.page = page
        self.width = width
        self.masks = masks or []
        self.offset = offset
        self.direction = direction
        self.description = description

    def get_label(self, state):
        return [mask.label for mask in self.masks if mask(state)]


class Fifo:
    def __init__(self, page, offset, depth, width=4, direction=IODIR.r, description=""):
        self.page = page
        self.offset = offset
        self.depth = depth
        self.width = width
        self.direction = direction
        self.description = description