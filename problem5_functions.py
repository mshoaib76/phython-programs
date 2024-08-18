def calculator(a,b,operator):
     if operator=='+':
         c=a+b
         print("addition of two number is :",c)
     elif operator=='-':
         c=a-b
         print("substriction of two number is ",c)
     elif operator=='*':
         c=a*b
         print("multipliction of two number is ",c)
     elif operator=='/':
         c=a/b
         print("division of two number is ",c)
     elif operator=='%':
         c=a%b
         print("reminder  of two number is ",c)
     else:
        print("invalid choice")

a=int(input("enter first number ;"))
b= int(input("enter second number ;"))
operator=input("enter a operation :")
calculator(a,b,operator)


