import random
import uuid
from enum import Enum
from os.path import abspath
from typing import List, Tuple

import numpy as np

import config

class SomeEntity:
    def __init__(self):
        self.foo = "bar"
        self.something_from_config = config.some_param