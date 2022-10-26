import os
import time
    
file = "file_stats.py"
st = os.stat(file)
print("file stats: ", file)
mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
print("- created:", time.ctime(ctime))
print("- last accessed:", time.ctime(atime))
print("- last modified:", time.ctime(mtime))
print("- Size:", size, "bytes")
print("- owner:", uid, gid)
print("- mode:", oct(mode))
