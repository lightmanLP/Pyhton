from forbiddenfruit import curse


Int = type("", (int,), {})
Str = type("", (str,), {})
document = type("", (), {"write": print})

for i in (int, str):
  curse(i, "__add__", lambda a, b: str(Str(a) + Str(b)))
  curse(i, "__sub__", lambda a, b: int(Int(a) - Int(b)))

document.write("1" - 1);
document.write(2 + "1");