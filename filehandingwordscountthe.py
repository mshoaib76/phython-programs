try:
 with open("C:\\Users\Shoaib Baloch\Desktop\phython\\notes.txt","r") as file:
# file.write("the is coding.the prof.Faisal saab is good .the uni of layyah is very bad .the flowers and greenry is not available in uni of layyah. ")
    lines =file.readlines()
    word_count=0
    for line in lines:
     word_count +=line.lower().count("the")
     print("total word count ",word_count)

except:
        print("file is not availbe")
