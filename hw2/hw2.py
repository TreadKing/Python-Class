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
num = int(input('Enter height of the triangle: '))
triangle(num)

#2
def palindromeChekcer(s):
    s = s.strip()
    s = s.replace(' ', '')
    s = s.lower()
    rev = ''.join(reversed(s))
    return(s == rev)

pal = input('Enter a string to check for palindrome: ')
output = palindromeChekcer(pal)
print(output)

#3
inputNum = input('input a space seperated list of numbers: ')
nums = inputNum.split()
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
nums.sort()
print('The second largest number:' + str(nums[len(nums)-2]))


#4
import random
rand = random.randint(0,4000)
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
file = open('bee.txt', 'r')
r1 = file.readlines()
count = 0
for e in r1:
    for i in range(0,len(e)):
        if(e[i].isupper()):
            count+=1
print('Number of uppercase characters in txt tile: ' + str(count))