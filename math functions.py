import math

number = float(input("Enter a decimal number here:"))
print("The floor and ceiling of", number, "are", str(math.floor(number)), "and", str(math.ceil(number)))

x = 7
y = -10
print("The result of copying the sign of y onto x is", math.copysign(x,y))

absvalue = int(input("Enter a number here:"))
print("The absolute value of", absvalue, "is", math.fabs(absvalue))

print("The GCD of 49 and 21 is", str(math.gcd(21, 49)))