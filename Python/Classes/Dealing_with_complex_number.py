'''For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.
The real and imaginary precision part should be correct up to two decimal places.
Input Format
One line of input: The real and imaginary part of a number separated by a space.
Output Format
For two complex numbers C and D. the output should be in the following sequence on separate lines:
C+D
C-D
CD
C/D
mod(C)
mod(D)
For complex numbers with non-zero real(A) and complex part(B), the output should be in the following format:
A+ Bi
Replace the plus symbol (+) with a minus symbol (-) when B < 0
For complex numbers with a zero complex part ie, real numbers, the output should be:
A+0.00%
For complex numbers where the real part is zero and the complex part(B) is non-zero, the output should be:
0.00+ Bi
Sample Input
21
56
Sample Output
7.00+7.001
-3.00-5.001
4.00+17.001
0.26-0.11i
2.24 + 0i
7.81+0.001'''
import math
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real,
        self.imaginary + no.imaginary)  
    def __sub__(self, no):
        return Complex(self.real - no.real,
        self.imaginary - no.imaginary)
    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
        self.real * no.imaginary + self.imaginary * no.real)
    def __truediv__(self, no):
        denom = no.real ** 2 + no.imaginary ** 2
        return Complex(
            (self.real * no.real + self.imaginary * no.imaginary) / denom,
            (self.imaginary * no.real - self.real * no.imaginary) / denom
        )
    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0.0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
