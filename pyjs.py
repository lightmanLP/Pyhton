from forbiddenfruit import curse


class OrigInt(int):
  pass


class OrigStr(str):
  pass


class _Updates:
  def str_add(a, b):
    return str(OrigStr(a) + OrigStr(b))

  def str_sub(a, b):
    return int(OrigInt(a) - OrigInt(b))

  def int_add(a, b):
    return str(OrigStr(a) + b)

  def int_sub(a, b):
    return int(OrigInt(a) - OrigInt(b))



curse(str, "__add__", _Updates.str_add)
curse(str, "__sub__", _Updates.str_sub)
curse(int, "__add__", _Updates.int_add)
curse(int, "__sub__", _Updates.int_sub)


print("1" - 1)
print(2 + "1")