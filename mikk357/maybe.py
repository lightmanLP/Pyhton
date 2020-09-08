import random


Maybe = type("Maybe", (), {
    "__bool__": lambda s: bool(random.getrandbits(1))
})()
