#hw2
#1
def triangle(n):
    k = 2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=' ')
        k -= 2
        for j in range(0,i*2+1):
            print('* ', end = '')
        print('\r')
num = int(input('Enther height of the triangle'))
triangle(num)

#2
def palindromeChekcer(s):
    rev = ''.join(reversed(pal))
    return(s == rev)

pal = input('Enter a string to check for palindrome')
output = palindromeChekcer(pal)
print(output)

#3
inputNum = input('How many numbers in the list')
nums = inputNum.split()
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
nums.sort()
print(nums[len(nums)-2])
print(nums)

#4
import random
rand = random.randint(0,4000)
print(rand)
def randomLine(a):
    file = open('bee.txt', 'r')
    r2 = file.readlines()
    file.close()
    if(r2[a].isspace()):
        randomLine(a-1) 
    else:
        print(r2[a])

randomLine(rand)

#5
import re
file = open('bee.txt', 'r')
r1 = file.readlines()
r = []
count = 0
for e in r1:
    for i in range(0,len(e)):
        if(e[i].isupper()):
            count+=1
    #r.extend(re.findall('([A-Z]+)',e))
print(count)







