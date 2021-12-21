#1) Palindrome check
def is_palindrome(text):
    return text[0:]==text[-1::-1]
#example
print(is_palindrome("madam"))

#2) Prime number check
def is_prime(num):
    if num==1 : return False
    for i in range(2,num):
        if (num%i==0) :
            return False
    else :
        return True
#example
print(is_prime(23))

#3) check if number is in range
def in_range(num,rng): #rng for range
    return ((min(rng)<=num) and (num<=max(rng)))
#example
Var=range(1,8) 
print(in_range(8,Var)) #note that 8 returns false since the function range doesn't include the second parameter

#4) Factorial
def fact(num):
    s=1
    if num>=0 :
        for i in range(1,num+1):
            s=s*i
        return s
    else : return("argument negative")
#example
print(fact(5))

#5) String reverser
def revers(str):
    return str[-1::-1]
#example
print(revers("amine"))

#6)Sum
#this function already exists it's "sum" but we're going to re-create it
def Sum(list):
    s=0
    for i in list :
        s+=i
    return s
#example
vect=[1,3,7,9]
print(Sum(vect))

#7)Max three numbers
#this function also exists "max" but it can take more/less than 3 arguments so we remake it to take exactly 3 without using "max"
def max_3(a,b,c):
    if a>b :
        if a>c :
            return a
        else :
            return c
    elif b>c :
        return b
    else :
        return c
#example
print(max_3(11,3,8))
