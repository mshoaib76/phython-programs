import os
if os.path.exists("C:\\Users\Shoaib Baloch\Desktop\phython\\A.txt"):
    os.remove("C:\\Users\Shoaib Baloch\Desktop\phython\\A.txt")
else:
    print("file not exists")

print("file deleted successfully")