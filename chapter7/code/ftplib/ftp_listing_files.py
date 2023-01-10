#!/usr/bin/env python3

from ftplib import FTP

ftp_client=FTP('ftp.be.debian.org')
print("Server: ",ftp_client.getwelcome())
print(ftp_client.login())
print("Files and directories in the root directory:")
ftp_client.dir()

ftp_client.cwd('/www.kernel.org/pub/linux/kernel/v6.x/')
files=ftp_client.nlst()
files.sort()
print("%d files in /pub/linux/kernel directory:"%len(files))
for file in files:
	print(file)

ftp_client.quit()

