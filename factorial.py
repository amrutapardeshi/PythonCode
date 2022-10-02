#The factorial of a number is the product of all the integers from 1 to that number.
#the factorial of 6 is 1*2*3*4*5*6 = 720 denoted by n!
def fact(num):
    if num ==1:
        return num
    else:
        return num * fact(num - 1)

y = int(input("Enter a number:"))
print(fact(y))
