import sys


__doc__ = """

    магический метод __getitem__
    в списках, кортежах, и наследниках отвечает
    за получение элемента по индексу
        list[index]
    в словарях отвечает за получение значения по ключу
        dict[key]
        dict[k1, k2] # будет искать ключ (k1, k2)

    так же при таком обращении к объекту выражения вида
        x: , :y , x:y , x::z , :y:z , x:y:z
    преобразуются в срезы slice(x | None, y | None, z | None)

"""

# простая версия, может только выводить строку
print = type("Printer", (), {
        "__getitem__": (lambda self, value: sys.stdout.write(value))
    })()

print["Hello World!\n"]


# если `затенили` встроенную функцию, то её можно вызвать так
__builtins__.print("\n\n")


# сложная версия
# принимает именованые аргументы, но не может выводить объекты типа slice
print = type("Printer", (), {
    "__getitem__": (lambda s, v: __builtins__.print(
        *filter(
            lambda o: not isinstance(o, slice),
            (v if isinstance(v, tuple) else (v,))
        ),
        **dict((i.start, i.stop) for i in v if isinstance(i, slice)))
    )})()

print["umm...\n", "\nGoodbye!", "sep":"\n...\n...\n...\n", "flush":True]


# ах, кстати, всё это можно сделать и без type и лямбда-методов,
# ...
# но я же из дурки сбежал

# Ш.У.Е!
