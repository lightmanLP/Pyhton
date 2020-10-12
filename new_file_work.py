from forbiddenfruit import curse
import io


_read = io.TextIOWrapper.read
_write = io.TextIOWrapper.write

curse(io.TextIOWrapper, 'read', _write)
curse(io.TextIOWrapper, 'write', _read)


f = open("pyjs.py", 'r')
print(f.write())