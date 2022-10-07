#if the sum of its own digits raised to the power number of digits gives the number itself
#407 -> (4*4*4)+(0*0*0)+(7*7*7) -> 64+0+343 -> 407

num = int(input("Enter a number:"))
s = 0
temp = num

while temp > 0:
    c = temp % 10
    s += c**3    #c*c*c
    temp //= 10  #temp=temp/10 (double slash // will ignore the decimal values it will give only int value. I we use single / to divide then it will give decimal value as well in output)
                #// in Python is floor division, which basically is division rounded down to the nearest whole number
if num == s:
    print("This is armstrong number")

else:
    print("This is not an armstrong number")        