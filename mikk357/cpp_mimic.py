import sys
import os


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
endl = os.linesep

def main():

    cout << "Hello World!" << endl;
    cout << "Do you want something?" << endl;

    x: str = str();
    x <<= cin;

    if (x == "yes"):
        cout << "But I have nothing. :(" << endl;

    if (x == "no"):
        cout << "Alright" << endl;

    cout << "Bye!" << endl;
    return 0;


if __name__ == '__main__':
    main()
