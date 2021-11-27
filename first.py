import random
number = (random.randint(0,100))
attempts = 0
while True:
    guess=int(input('What do you think the number is? \n'))
    attempts+=1
    if guess < number:
        print("too low")

    elif guess > number:
        print("too high")

    else:
        break
        
print('you got the number in', attempts, 'guesses')

