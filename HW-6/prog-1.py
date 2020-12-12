import os
import sys
import time

path = sys.argv[1]
while True:
    print(os.path.exists(path))
    time.sleep(5)
    