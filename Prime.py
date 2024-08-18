from math import sqrt
def is_prime(n):
    if n<2:
        return False
for i in range(2,int(sqrt(n))+1):
    if n%i==0:
                return False
return True

prime_count =0
prime_numbers=[]

for i in range(3,10000,2):
    if is_prime(i):
        prime_count +=1
        prime_numbers.append(i)
        if prime_count %50==0:
            print(f"{prime_count}prime numbers found so for")
            if prime_count==450:
                break
    print(f"the 450th prime numbers is {prime_numbers[-1]}")
