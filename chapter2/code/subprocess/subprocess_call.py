#!/usr/bin/python3
import os
from subprocess import call

print("Current path",os.getcwd())
print("PATH Environment variable:",os.getenv("PATH"))

print("List files using the subprocess module:")
call(["ls", "-la"])


