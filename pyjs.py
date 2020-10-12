from forbiddenfruit import curse


Int = type("", (int,), {})
Str = type("", (str,), {})


def add(a, b):
  """  """

  return str(Str(a) + Str(b))


def sub(a, b):
  """  """
  
  return int(Int(a) - Int(b))


document = type('', (), {'write': print})
for i in (int, str):
  curse(i, "__add__", add)
  curse(i, "__sub__", sub)

document.write("1" - 1);
document.write(2 + "1");