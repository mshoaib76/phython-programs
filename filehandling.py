# f=open("C:\\Users\\Shoaib Baloch\\Desktop\\phython\A.txt","w")
#f=open("C:\\Users\\Shoaib Baloch\\Desktop\\phython\A.txt","r")      # w mean write ,x mean empty ,r mean read
#f.write("Hello this is shoaib baloch")
#print("file wrote successfully......")
#print(f.read(25))
#print(f.readline())     it can print only first line
#print(f.readlines())     it can print all lines



# for exciption handling we use try catch block
# if any file not available but if we access than it show rantime error that's why we use exciption handling
# Example is given below
try:
    f=open("C:\\Users\\Shoaib Baloch\\Desktop\\phython\A.txt","r")
    print(f.read(30))
except:
    print("files not found ")
else:
    f.close()
    print("your file is closed")