#Palindrome phrase number or a sequence will be same even if it is written in backwards
#MADAM
def pal(num):
    x1 = num[::-1]
    if x1 == num:
        print('This is a palindrome')
    else:
        print('This is not a palindrome')

y = input("Enter a word:")
print(pal(y))        
