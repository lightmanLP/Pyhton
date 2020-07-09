from collections import UserString
from typing import List
import sys
import os


__doc__ = """

    Вы думали это С++?
    НО ЭТО БЫЛ Я, PYTHON!

"""


class string(UserString):
    def __init__(self, seq: str = ""):
        super().__init__(seq)


class coutClass:
    def __lshift__(self, value):
        """ перегрузка self << value """
        sys.stdout.write(value)
        return self


class cinClass:
    def __rshift__(self, value):
        """ перегрузка self >> value """
        value.data = input()


cout = coutClass()
cin = cinClass()
endl = os.linesep


def main(argc: int, argv: List[str], envp: List[str]) -> int:

    cout << "Hello World!" << endl;
    cout << "Do you want something?" << endl;

    x: string = string();
    cin >> x;

    if (x == "yes"):
        cout << "But I have nothing. :(" << endl;

    if (x == "no"):
        cout << "Alright" << endl;

    cout << "Bye!" << endl;
    return 0;


if __name__ == "__main__":
    main()
