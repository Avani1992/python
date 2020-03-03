import os
from datetime import *

t=os.stat("abc1.txt")
print(t.st_size)
print(datetime.fromtimestamp(t.st_mtime))
print(datetime.fromtimestamp(t.st_atime))