# To delete an entire folder, use the os.rmdir() method:
import os

try:
    os.rmdir("myfolder")
except:

    print('file does not exits or file has already been deleted')
    pass
