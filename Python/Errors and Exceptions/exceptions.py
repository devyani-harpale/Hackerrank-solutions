'''Exceptions
Errors detected during execution are called exceptions.
Examples:
Zero DivisionError
This error is raised when the second argument of a division or modulo operation is zero.
>>> a = '1'
>>> b = '0'
>>> print int(a) / int(b)
>>> ZeroDivisionError: integer division or modulo by zero
ValueError
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
>>> a = T'
>>> b = 44'
>>> print int(a) / int(b)
>>> ValueError: invalid literal for int() with base 10:
To learn more about different built-in exceptions click here.
Handling Exceptions
The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.
#Code
try:
print 1/0
except ZeroDivisionError as e:
print "Error Code:",e'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

for _ in range(N):   
    try:
        a, b = map(int, input().split())
        print (a//b)
        
    except Exception as e:
        print("Error Code:", e)