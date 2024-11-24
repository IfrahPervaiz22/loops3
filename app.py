import math
total=0
for i in range(1,8):
   total+=2*(i/math.factorial(i))
print("Sum of First seven terms twice", total)