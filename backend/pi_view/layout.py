
class Block:
    def __init__(self, blocks=None, registers=None, fifos=None, description=""):
        self.description = description

        self.fifos = fifos or []
        self.blocks = blocks or []
        self.registers = registers or []
