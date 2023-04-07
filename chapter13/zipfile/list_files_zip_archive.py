import zipfile

def list_files_in_zip(filename):
    with zipfile.ZipFile(filename) as thezip:
        for zipinfo in thezip.infolist():
            yield zipinfo.filename
                
for filename in list_files_in_zip("zipfile.zip"):
    print(filename)
