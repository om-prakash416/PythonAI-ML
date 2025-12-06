#if else ,elseif


#voting example
age =21
if age>=18:
    print("can vote")
    
    
#traffic light example
color =(input('enter color: '))

if color =='red':
    print('stop')    
elif color == 'yellow':
    print('get ready')
elif color == 'green':  
    print('go')
else:
    print('wrong color')
    
    
##real life example
    
username =input('enter username: ')
password =input('enter password: ') 

if username =='admin' and password =='admin123':
    print('login successful')
elif username !='admin':
    print('invalid username')
elif password !='admin123':
    print('invalid password')
else:
    print('login failed')
    
    
#check if a number is divisible by 5
    number =int(input('enter a number: '))
    
    if number%5==0:
        print('divisible by 5')
    else:
        print('not divisible by 5')
        
        
#check if a number is even or odd
    num =int(input('enter a number: '))
    
    if num%2==0:
        print('even number')
    else:
        print('odd number')
        
        
#check if a year is leap year or not
    year =int(input('enter a year: '))
    
    if year%4==0:
        print('leap year')
    else:
        print('not leap year')  
        
#check grade based on marks
    marks =int(input('enter marks: '))
    if marks>=90:
        print('grade A')
    elif marks>=80:
        print('grade B')
    elif marks>=70:
        print('grade C')
    elif marks>=60:
        print('grade D')
    else:
        print('Invalid marks')
        
        
        
#check largest of three numbers
    a =int(input('enter first number: '))
    b =int(input('enter second number: '))
    c =int(input('enter third number: '))
    
    if a>b and a>c:
        print('a is largest')
    elif b>a and b>c:
        print('b is largest')
    else:
        print('c is largest')
        
        
#check if a character is vowel or consonant
    char =input('enter a character: ')
    if char in 'aeiouAEIOU':
        print('vowel')
    else:
        print('consonant')
        
        
#check if a number is positive, negative or zero
    num =int(input('enter a number: '))
    
    if num>0:
        print('positive number')
    elif num<0:
        print('negative number')
    else:
        print('zero')
        
#check if a person is eligible for a senior citizen discount
    age =int(input('enter age: ')) 
    if age>=60:
        print('eligible for senior citizen discount')
    else:
        print('not eligible for senior citizen discount')   
        
#check if a character is uppercase or lowercase
    char =input('enter a character: ')
    if char.isupper():
        print('uppercase')
    else:
        print('lowercase')    
        
#check if a year is a leap year or not  
    year =int(input('enter a year: '))
    
    if (year%4==0 and year%100!=0) or (year%400==0):
        print('leap year')
    else:
        print('not leap year')
        
#check if a number is prime or not
    num =int(input('enter a number: '))
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print('not prime')
                break
        else:
            print('prime')
    else:
        print('not prime')
        
        
#check if a string is palindrome or not
    string =input('enter a string: ')
    if string==string[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
        
#check if a number is Armstrong or not
    num =int(input('enter a number: ')) 
    sum =0
    temp =num
    while temp>0:
        digit =temp%10
        sum +=digit**3
        temp //=10
    if num==sum:
        print('Armstrong number')
    else:
        print('not Armstrong number')
        
#check if a number is perfect or not
    num =int(input('enter a number: '))
    sum =0
    for i in range(1,num):
        if num%i==0:
            sum +=i
    if sum==num:
        print('perfect number')
    else:
        print('not perfect number')
        
#check if a character is alphabet or not
    char =input('enter a character: ')
    if char.isalpha():
        print('alphabet')
    else:
        print('not alphabet')
        
        
#check if a number is even or odd using ternary operator
    num =int(input('enter a number: '))
    result = 'even' if num%2==0 else 'odd'
    print(result)
    
    
#check if a number is positive, negative or zero using nested if else
    num =int(input('enter a number: '))
    if num>0:
        print('positive number')
    else:
        if num<0:
            print('negative number')
        else:
            print('zero')
            

