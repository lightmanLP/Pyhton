import random


maybe = type("Maybe", (int,), {
    "__bool__": lambda s: bool(random.getrandbits(1))
})

Maybe = maybe()


if __name__ == "__main__":
    hexdigits = "0123456789ABCDEF"

    def char():
        for i in hexdigits[1:]:
            if Maybe:
                if Maybe:
                    return i
        else:
            return hexdigits[0]

    for i in range(4):
        print(f"{char()}{char()} ", end="")
    print()
