import sys


__doc__ = """

    Вы думали это С++?
    НО ЭТО БЫЛ Я, PYTHON!

"""


class coutClass:
    def __lshift__(self, value):
        """ перегрузка self << value """
        sys.stdout.write(value)
        return self


class cinClass:
    def __rlshift__(self, value) -> str:
        """ перегрузка value << self """
        return input("")


cout = coutClass()
cin = cinClass()


def main():

    cout << "Hello World!\n" << "Do you want something?\n";

    x: str = str();
    x <<= cin;

    if (x == "yes"):
        cout << "But I have nothing. :(\n" << "Bye!\n";

    if (x == "no"):
        cout << "Alright\n" << "Bye!\n";

    return 0;


if __name__ == '__main__':
    main()
