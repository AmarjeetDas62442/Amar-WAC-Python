#  is used for single line comment

'''
    is 
    used for
    multiline command
'''

#First Code
# print ("Hello, World!!")

# print ("hello", end = " ") # the space in end connects family to hello
# print ("family")

# print ("hello","family!!") # , used to join strings

# print("hello", end="\n") # \n is used for next line
# print ("family!")

#print('today', 'is', 'first', 'class', sep='\n') # sep argument is used for distinguishing the gap b/w strings

#How to take inputs
# n = input("Enter Name :")
# print (n)

# n = str(input("enter string : "))
# print('You said =', n)

# n = int(input("enter int :"))
# print (n)

# n = float(input("enter float :"))
# print (n)

'''
    VARIABLES & DATATYPES
'''

# Datatypes - int, float, string, bool

# a = True
# print (a)
# print (type (a)) # type function is used to specify the type of variable i.e. the datatype

# a = 15.69
# print (a)
# print (type (a))

'''
Typecasting
'''
# By default, python reads all inputs as strings

# n = int(input()) # explicit Typecasting
# print (n)
# print (type(n))


'''
Operators - Arithmetic & Logical
    1. Arithmetic
        add +
        subtract -
        multiply *
        divide /
        integer divide //
        power **
        modulo % (gives remainder)

    2. Logical
        OR
        AND
        NOT
    
    3. Comparison
        >
        <
        == (equals to)
        >=
        <=
        != (not equals to)
'''

'''
 USING ARITHMETIC OPERATORS
'''
# a=20
# b=5
# print("sum = ", a+b)
# print("sub = ", a-b)
# print("mult = ", a*b)
# print("quotient = ", a/b) # / gives floating values
# print("int divide = ", a//b) # // gives int values
# print("remainder = ", a%b)
# print("power = ", a**b)
# print("sq root of a =", a**0.5)

# s = "today"
# print (s+s) # + is used to concatenate

# s = "today"
# print (5*s) # today printed five times

# s = "today"
# print (5*(s + " ")) 

'''
 USING LOGICAL OPERATORS
'''
# print (0 or 1) # prints 1
# print (0 and 1) # prints 0
# print (False and True) # prints false
# print (False or True) # prints True

'''
Conditional Statements
 1. IF ELSE
    if (statement):
        statement
    else :
        statement
'''

# 1. Odd/Even number
# n = int(input())
# if (n%2==0):
#     print ("Even")
# else :
#     print ("Odd")

'''
while doing a%b range is [a, b-1]
'''

# 2. Remainder
# n = int(input())
# if n%3==0 :
#     print ("zero")
# elif n%3==1 :
#     print ("one")
# else :
#     print ("two")

# 3. multiple of 3 is fizzbuzz, multiple of 3 is fizz, multiple of 5 is buzz
# n = int(input("Enter : "))
# if n%3==0  and n%5==0 :
#     print ("FizzBuzz")
# elif n%3==0 :
#     print ("Fizz")
# elif n%5==0 :
#     print ("Buzz")
# else :
#     print (n)

# 4. Calculator
# a = int(input("Enter a No. = "))
# b = int(input("Enter b No. = "))
# oper = input("Choose operator : ")
# if oper == '+' :
#     print (a+b)
# elif oper == '-' :
#     print (a-b)
# elif oper == '*' :
#     print (a*b)
# elif oper == '/' :
#     print (a/b)
# else :
#     print ("wrong")

# 5. Leap Year
# y = int(input("Enter Year : "))
# if y%400 == 0 :
#     print("Leap")
# else :
#     if y%100 == 0 :
#         print("Not Leap")
#     elif y%4 ==0 :
#         print("Leap")
#     else :
#         print("Not Leap")

'''
Loops - For, While

    1. While loop (syntax)
       i = 0 --> counter
       while i < 10 : --> condition
            print("statement")
            i = i+1 --> Step size

    2. For loop (syntax)
'''

# While Loop
# i=0
# while i < 10 :
#     print ("Amar")
#     i=i+1
#     print ("Das")

# i=0
# while i < 10 :
#     print ("Amar", end = " ")
#     i=i+1

# i=0
# while i < 10 :
#     print ("Amar")
#     print ("Das")
#     i=i+1

# i=0
# while i < 10 :
#     print ("Amar")
#     print ("Das")
#     i=i+2
    
'''
range() function (syntax)
    range (start= ,stop= ,step=)
'''

# print (list(range(0,15,1)), end = " ")

# for i in range(10) :
#     print(i)

# 6. Multiplication table of a given number
# n = int(input("Enter a Number : "))
# for i in range (1, 11) :
#     print (n*i)


    
