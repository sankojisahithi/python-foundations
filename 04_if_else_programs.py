#Even or Odd
n=int(input("Enter number:"))
if(n%2==0):
    print("Number",n, "is even")
else:
    print("Number",n, "is odd")

#Positive or Ngative
n=int(input("Enter number:"))
if(n>0):
    print("Number",n, "is positive")
elif(n<0):
    print("Number",n, "is negative")
else:
    print("Number",n, "is zero")

#Greater
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):    
     print("b is greater")
else:
     print("c is greater")

#Simple Calculator
a=int(input("Enter a:")) 
b=int(input("Enter b:"))
op=input("Enter operator(+,-,*,/):")
if(op=='+'):
    print("Result",a+b)
elif(op=='-'):
    print("Result",a-b)
elif(op=='*'):    
    print("Result",a*b)
else:
    print("Result",a/b)

#Leap year
year=int(input("Enter year:"))
if(year%4==0 or year%400==0 and year%100!=0):
    print("Leap year")
else:
    print("Not Leap year")

#Grade
marks=int(input("Enter marks:"))
if(marks>90 and marks<=100):
    print("Grade 'A'")
elif(marks>80 and marks<=90):  
    print("Grade 'B'")  
elif(marks>70 and marks<=80):
    print("Grade 'C'")
else:
    print("Fail")
    
#Vowel or Consonant
ch=input("Enter vowel or consonant:").lower()
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("Vowel")
else:
    print("Consonant")