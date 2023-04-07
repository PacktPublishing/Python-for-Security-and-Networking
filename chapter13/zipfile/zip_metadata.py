import datetime 
import zipfile 
zf = zipfile.ZipFile("zipfile.zip", "r") 
for info in zf.infolist(): 
    print(info.filename) 
    print("  Comment: " + str(info.comment.decode())) 
    print("  Modified: " + str(datetime.datetime(*info.date_time))) 
    print("  System: " + str(info.create_system) + " (0=MS-DOS OS-2, 3=Unix)") 
    print("  ZIP version: " + str(info.create_version)) 
    print("  Compressed: " + str(info.compress_size) + " bytes") 
    print("  Uncompressed: " + str(info.file_size) + " bytes") 
zf.close() 
