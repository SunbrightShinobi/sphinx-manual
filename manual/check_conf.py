import py_compile
import sys

try:
    py_compile.compile('source/conf.py', doraise=True)
except Exception as e:
    print("❌ conf.py syntax error:\n")
    raise
else:
    print("✅ conf.py syntax OK")
