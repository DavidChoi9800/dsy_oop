<Exercise 1: For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.<br>

<b>Input Format</b><br>

One line of input: The real and imaginary part of a number separated by a space.

<b>Output Format</b><br>

For two complex numbers C and D, the output should be in the following sequence on separate lines:<br>
* C + D
* C - D
* C * D
* C / D
* mod(C)
* mod(D)

For complex numbers with non-zero real (A)and (B)complex part, the output should be in the following format: 
~~~
A + Bi
~~~
Replace the plus symbol (+) with a minus symbol(-)  when B < 0.
For complex numbers with a zero complex part i.e. real numbers, the output should be: 
~~~
A + 0.00i
~~~


For complex numbers where the real part (B) is zero and the complex part (B) is non-zero, the output should be:
~~~
0.00 + Bi
~~~

<b>Sample Input</b>

~~~
2 1 
5 6
~~~


<b>Sample Output</b>
~~~
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
~~~

<b>Concept</b>


Python is a fully object-oriented language like C++, Java, etc. For reading about classes, refer here. <br>
<br>
Methods with a double underscore before and after their name are considered as built-in methods. They are used by interpreters and are generally used in the implementation of overloaded operators or other built-in functionality. 
~~~
__add__-> Can be overloaded for + operation
~~~

~~~
__sub__ -> Can be overloaded for - operation
~~~

~~~
__mul__ -> Can be overloaded for * operation
~~~


<b>Initial Code</b>
~~~
import math

class Complex(object):
    def __init__(self, real, imaginary):
        
    def __add__(self, no):
        
    def __sub__(self, no):
        
    def __mul__(self, no):

    def __truediv__(self, no):

    def mod(self):

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

if __name__ == '__main__':
~~~