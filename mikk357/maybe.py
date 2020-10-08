import random


Maybe = type("Maybe", (bool,), {
    "__bool__": lambda s: bool(random.getrandbits(1))
})()
