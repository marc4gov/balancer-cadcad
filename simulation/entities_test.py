import unittest
import uuid
from unittest.mock import MagicMock, patch

import utils
from entities import SomeEntity



class TestSomeEntity(unittest.TestCase):
    def test_init_from_config(self):
        entity = SomeEntity()
        self.assertEqual(entity.something_from_config,1)


if __name__ == '__main__':
    unittest.main()
