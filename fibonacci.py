#The Fibonacci sequence is a type series where each number is the sum of the two that precede it.
#The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

n = int(input("Enter the number of elements:"))
print(a,b,end=" ")
while n - 2:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    n = n - 1
    
