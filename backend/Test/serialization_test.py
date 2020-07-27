import os
import json
from unittest import TestCase, main

from piView.loader import Loader, JSONEncoder, example



class TestSerialization(TestCase):

    def test_load(self):
        # Act
        block = Loader.load(example)

    def test_json_dump(self):
        # Arange
        block = Loader.load(example)

        # Act
        result = json.dumps(block, cls=JSONEncoder)

        # Assert
        self.assertIn('registers', result)
        self.assertIn('fifos', result)


if __name__ == '__main__':
    main([])
