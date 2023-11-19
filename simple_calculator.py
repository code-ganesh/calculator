def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("Select your operation\n "
      "1.Addition\n "
      "2.Subtraction\n "
      "3.Multiplication\n "
      "4.Division")
num=int(input("Enter a choice\t"))
op_1=int(input("Enter first operator\t"))
op_2=int(input("Enter second operator\t"))
if num==1:
    print("The sum is:",add(op_1,op_2))
elif num==2:
    print("The difference is:",subtract(op_1,op_2))
elif num==3:
    print("The product is:",multiply(op_1,op_2))
elif num==4:
    print("The quotient is:",divide(op_1,op_2))
else:
    print("Invalid Input")

