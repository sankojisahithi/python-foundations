#1.datatypes
"""integer=5
float=12.6
string="sahithi"
boolean=True
print(type(integer))
print(type(float))
print(type(string))
print(type(boolean))
print("--------")"""

#2.Typecasting
num_str="5"
num_int=int(num_str)
num_float_val = float(num_int)
print(num_str, type(num_str))
print(num_int, type(num_int))
print(num_float_val, type(num_float_val))
print("----------")

# Conditional statements
marks = int(input("Enter marks:"))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")