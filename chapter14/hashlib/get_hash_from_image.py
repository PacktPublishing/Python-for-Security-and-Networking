#!/usr/bin/env python3
import hashlib

md5 = hashlib.new("md5")
sha256 = hashlib.new("sha256")
with open("python-logo.png", "rb") as some_file:
    md5.update(some_file.read())
    print("MD5:",md5.hexdigest())
    print("SHA256:",sha256.hexdigest())

