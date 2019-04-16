import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        new_real = self.real + other.real
        new_imaginery = self.imaginary + other.imaginary
        return Complex(new_real, new_imaginery)

    def __sub__(self, other):
        new_real = self.real - other.real
        new_imaginery = self.imaginary - other.imaginary
        return Complex(new_real, new_imaginery)

    def __mul__(self, other):
        new_real = (self.real * other.real) - (self.imaginary * other.imaginary)
        new_imaginery = (self.real * other.real) + (self.imaginary * other.imaginary)
        return Complex(new_real, new_imaginery)

    def __truediv__(self, other):
        new_real = ((self.real * other.real) + (self.imaginary * other.imaginary)) / (other.real**2 + other.imaginary**2)
        new_imaginery = ((self.imaginary * other.real) - (self.real * other.imaginary)) / (other.real**2 + other.imaginary**2)
        return Complex(new_real, new_imaginery)

    def mod(self):
        new_real = math.sqrt( self.real**2 + self.imaginary**2 )
        return Complex( new_real, 0 )

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

if __name__ == "__main__":
    a, b = input().split()
    a, b = float( a ), float( b )
    C = Complex( a, b )

    a, b = input().split()
    a, b = float( a ), float( b )
    D = Complex( a, b )

    print( C + D )
    print( C - D )
    print( C * D )
    print( C / D )
    print( C.mod() )
    print( D.mod() )
