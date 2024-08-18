#for copy files 
try:
    with open("C:\\Users\\Shoaib Baloch\\Desktop\\phython\A.txt") as f2:
      with open("C:\\Users\\Shoaib Baloch\\Desktop\\phython\B.txt","w") as f3:
        for i in f2:
            f3.write(i)

except:
    print("files not found ")
else:
    f2.close()
    print("your file is closed")