import ast
import random
import string

class BaseObfuscator(ast.NodeTransformer):
    """Base class providing helper methods."""
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
    
    def _random_string(self, length=6):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
