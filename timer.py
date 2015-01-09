import time
import sys
from importlib import import_module
start_time = time.time()
import_module("problem"+sys.argv[1])
print(time.time() - start_time)