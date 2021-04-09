#Melanie R. Morataya
#Working with an If Statement
num = int(input('Enter a number from -10 to 10: ')) 
if num < 0: 
    print(num, 'is negative')
print()

num = int(input('Enter another number from -10 to 10: ')) 
if num > 0: 
    print(num, 'is positive') 
    print(num, 'squared is ', num * num) 
print('Bye')
print()

#Else in an If Statement
num = int(input('Enter another number from -10 to 10: ')) 
if num < 0: 
    print('Its negative') 
else: 
    print('Its not negative')
print()

num = int(input('Enter another number from -10 to 10: ')) 
if num < 0: 
    print('Its negative') 
else: 
    print('Its not negative')
print()

#The use of Elif
jar = float(input("Enter how much you have in your money jar: ")) 
if jar == 0: 
    print("Sorry, you do not have savings") 
elif jar < 500: 
    print('Goof job') 
elif jar < 1000: 
    print('WoW!, Thats a tidy sum') 
elif jar < 10000: 
    print('Welcome Sir!') 
else: 
    print('Thank you')
print()

#Nesting if Statement
snow = True 
temp = -1 
if temp < 0: 
    print('It is freezing') 
    if snow: 
        print('Put on boots') 
    print('Time for Hot Choco') 
print('Bye')
print()

#If Expressions
age = 18 
status = None 
if (age > 12) and age < 20: 
    status = 'teenager' 
else: 
    status = 'not teenager' 
print(status)
print()

status = ('teenager' if age > 12 and age < 20 else 'not teenager') 
print(status)


