#Melanie R. Morataya
#While Loop
count = 0
print('Starting....')
while count < 8:
    print(count, ' ', end='')
    count += 1
print('Done!')
print()

#For Loop
print('Printing out values in a range....')
for i in range(0, 8):
    print(i, ' ', end='')
print('Done!')
print()

print('Printing out values in a range with an increment of 2....')
for i in range(0, 7, 2):
    print(i, ' ', end='')
print('Done')
print()

for _ in range(0,7):
    print('*', end='')
print()
print()

#Break Loop Statement
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 8):
    if i == num:
        break
    print(i, ' ', end='')
print('Done')
print()

num = int(input('Enter another number to check for: '))
for i in range(0, 8):
    if i == num:
        break
    print(i, ' ', end='')
print('Done')
print()

#Continue Loop Statement
for i in range(0, 8):
    print(i, ' ', end='')
    if i % 2 == 1:
        continue
    print('hey!! its an even number')
print('Done')
print()

#For Loop with Else
print('Print code only if all iterations are completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 5):
    if i == num:
        break
    print(i, ' ', end='')
else:
    print('All iterations successful')
print()

#Dice Roll Game 
import random

MIN = 1
MAX = 6

roll_again = 'yes'

while roll_again == 'yes':
    print('Rolling the dices...')
    print('The values are....')
    dice1 = random.randint(MIN, MAX)
    print(dice1)
    dice2 = random.randint(MIN, MAX)
    print(dice2)
    roll_again = input('Do you want to roll the dices again? (yes/no): ')
print()

