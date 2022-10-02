def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

#menu
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))
a = int(input("Enter first no: "))
b = int(input("Enter second no: "))

if ch==1:
    print(add(a, b))

elif ch==2:
    print(sub(a, b))
    
elif  ch==3:
    print(mul(a, b))
    
elif ch==4:
    print(div(a, b))
    
else:
    print("Invalid Choice")
