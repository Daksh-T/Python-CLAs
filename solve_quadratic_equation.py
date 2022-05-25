import cmath

a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is c? "))

D = (b**2) - (4*a*c)

#two solutions of the quadratic equation
sol1 = (-b+cmath.sqrt(D))/2*a
sol2 = (-b-cmath.sqrt(D))/2*a

print("The Discriminant is : ", D,)
print("The first solution is : ", sol1)
print("The second solution is : ", sol2)