
#types of loops in python
#1. for loop
#2. while loop

#while loop 
count =1
while (count<=5):
    print('Hello', count)
    count +=1   

count1 =5

while (count1>=1):
    print('Hi', count1)
    count1 -=1
    
#for loop
for i in range(1,6):
    print('Welcome', i)
    
    
for j in range(5,0,-1):
    print('Python', j)
    
    
#nested loop
for i in range(1,4):
    for j in range(1,4):
        print(i, j) 
        
 
#loop through a string
string ='hello'
for i in string:
    print(i)

#loop through a list
fruits =['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
    
#loop through a dictionary
person ={'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(key, value)
    
    
#loop through a set
colors ={'red', 'green', 'blue'}
for color in colors:
    print(color)
    
#loop through a tuple
numbers =(1, 2, 3, 4, 5)    
for num in numbers:
    print(num)  
    
#break and continue statements
for i in range(1, 11):
    if i == 5:
        break
    print(i)
    
for j in range(1, 11):
    if j == 5:
        continue
    print(j)
    
#nested loop with break
for i in range(1, 4):   
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)


#nested loop with continue
for i in range(1, 4):   
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)
        
#loop with else
for i in range(1, 6):
    print(i)
else:
    print('Loop completed')
    
#star pattern using loops

n =5
for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print() 
    
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('*', end=' ')
    print() 
    
#factorial of a number using loop
num =5    
factorial =1
for i in range(1, num+1):
    factorial *=i
print('Factorial of', num, 'is', factorial) 

#fibonacci series using loop
n =10
a, b =0, 1
for i in range(n):
    print(a, end=' ')
    a, b =b, a + b
print()

#sum of natural numbers using loop
n =10   
sum =0
for i in range(1, n+1):
    sum +=i
print('Sum of first', n, 'natural numbers is', sum)


#multiplication table using loop
num =7
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)
#reverse a number using loop
num =1234
reverse =0    
while num !=0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print('Reversed number is', reverse)


#check if a number is palindrome using loop
num =121
temp =num   
reverse =0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
    
if num == reverse:
    print(num, 'is a palindrome')
else:
    print(num, 'is not a palindrome')
    
    
#check if a number is prime using loop
num =29
is_prime =True      

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime =False
        break
if is_prime and num > 1:
    print(num, 'is a prime number')
else:
    print(num, 'is not a prime number')
    
#find gcd of two numbers using loop
a =56
b =40
while b != 0:
    a, b = b, a % b
print('GCD of', a, 'and', b, 'is', a)

#find lcm of two numbers using loop
a =12   
b =18
lcm =max(a, b)    
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm +=1
print('LCM of', a, 'and', b, 'is', lcm) 


#start print pattern all types different patterns
n =5
#pattern 1  
for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()
    
#pattern 2
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()
    
#pattern 3
for i in range(1, n+1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print('*', end=' ')
    print()
    
#pattern 4
for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print('*', end=' ')
    print()
    
#pattern 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
    
#pattern 6
for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
    
#pattern 7
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j >= i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
#pattern 8
for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if j >= i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    
#pattern 9
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
    
#pattern 10
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
#pattern 11
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print(k, end=' ')
    print()
    
#pattern 12
for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print(k, end=' ')
    print()
    
#pattern 13
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end=' ')
        else:
            print(j - (n - i), end=' ')
    print() 
    
    
#pattern 14
for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end=' ')
        else:
            print(j - (n - i), end=' ')
    print()
    
#pattern 15
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()
    
#pattern 16
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(i, end=' ')
    print()
    
    
#pattern 17
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print(i, end=' ')
    print()
    
    
#pattern 18
for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print(i, end=' ')
    print()
    
#pattern 19 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end=' ')
        else:
            print(i, end=' ')
    print()
    
#pattern 20
for i in range(n, 0, -1):
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end=' ')
        else:
            print(i, end=' ')
    print()
    
#pattern 21
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i + j - 1, end=' ')
    print()
    
    
i =1

while (i<=10):
    if(i%3==0):
        i+=1
        continue
    
    print('This will not be printed')
    i+=1
    
print('Loop ended')