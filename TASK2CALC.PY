def subtract(a,b):
    return a-b
def add(a,b):
    return a+b
def divide(a,b):
    if b == 0:
     return
    return a/b
def multiply(a,b):
    return a*b

print("My Calculator")
numx= float(input("Enter the First number: "))
numy=float(input("Enter the second number: "))

print("Choose operation: ")
print("A. SUBTRACTION")
print("B. ADDITION")
print("C. DIVISION")
print("D. MULTIPLICATION")

choice=input("Enter choice (A/B/C/D): ")

if choice =='A':
    result= subtract(numx, numy)
    operation='-'
elif choice =='B':
    result= add(numx,numy)
    operation='+'
elif choice =='C':
    result = divide(numx,numy)
    operation='/'
elif choice =='D':
    result= multiply(numx,numy)
    operation='*'
    
print(f"{numx} {operation} {numy} = {result}")

print("Thank You Prashant")
    