import sys


__doc__ = """

    магический метод __getitem__ отвечает за получение элемента по индексу
    object[index]

"""


print = type("Printer", (), {
        "__getitem__": (lambda self, value: sys.stdout.write(value))
    })()


print["Hello World!\n"]
