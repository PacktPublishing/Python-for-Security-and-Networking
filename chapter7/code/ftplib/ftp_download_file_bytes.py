#!/usr/bin/env python3

from ftplib import FTP

ftp_client=FTP('ftp.be.debian.org')
ftp_client.login()
ftp_client.cwd('/www.kernel.org/pub/linux/kernel/v6.x/')
ftp_client.voidcmd("TYPE I")
datasock,estsize=ftp_client.ntransfercmd("RETR ChangeLog-6.0")
transbytes=0
with open('ChangeLog-6.0','wb') as file_descryptor:
    while True:
        buffer=datasock.recv(2048)
        if not len(buffer):
            break
        file_descryptor.write(buffer)
        transbytes +=len(buffer)
        print("Bytes received",transbytes,"Total",(estsize,100.0*float(transbytes)/float(estsize)),str('%'))
datasock.close()
ftp_client.quit()
