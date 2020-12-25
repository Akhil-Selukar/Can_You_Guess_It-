import random

target = random.randint(1,100)
guess = [0]

print('++++++++++CAN YOU GUESS IT?++++++++++\n')
print('-------------------------------------')
print("\nI'm thinking of a number between 1 and 100")
print("Let's see how quickly you can guess it.")
print('\nYou will have to enter your guess till you guess the number correct.')
print('Number of guesses you take will be your score. tyr to keep it as low as possible.')
print('\nRULES:')
print('1. If you enter number less that 1 or greater that 100. It will be taken as invalid guess and will not be counted.')
print('2. After first valid guess it will give you a hint how close you are.')
print('3. If you are going towards the number it will say "You are getting closer to the number :)"')
print('4. If you are going away from the number it will say "You are going away from number :("')
print('-------------------------------------')
print('\nARE YOU READY ???')

while True:
    user_ip = int(input("Enter your guess : "))
    print(user_ip)

    if user_ip < 1 or user_ip > 100:
        print('Invalid guess, please enter guess between 1 to 100.')
        continue

    if user_ip == target:
        print('Your got {} correct in just {} guess'.format(target,len(guess)))
        break

    guess.append(user_ip)

    if not guess[-2]:
        if abs(target-user_ip) <=10:
            print('Doing good, the number is within +/-10 places.')
        else:
            print('Good guess but you need to search more.')
    else:
        if abs(target-guess[-1]) < abs(target-guess[-2]):
            print('You are getting closer to the number :)')
        else:
            print('You are going away from number :(')
