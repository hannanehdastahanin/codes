
import math

def t(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 3)

            triangle_type = "Equilateral" if a == b == c else "Isosceles" if a == b or a == c or b == c else "Scalene"
            triangle_type += " right" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else ""

            r=(f" {area:.3f}  {triangle_type}")
            return r
        else:
            print("invalid edges!")
a= int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
print(t(a,b,c))

