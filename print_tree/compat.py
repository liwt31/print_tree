import sys

PY2 = int(sys.version[0]) == 2

if PY2:
    CompatRecursionError = RuntimeError
else:
    CompatRecursionError = RecursionError
