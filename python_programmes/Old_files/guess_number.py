#! python3

# The guessing number game
import random, sys

print('Welcome to the number-guessing game! What is your name?  ') # Ask for name
name = input()
print('')
print('Hi, ' + name)

while True:
    print('Please specify the range of the number-guessing game.') # Ask for range of number
    try:
        low_lim = int(input('Lower boundary: '))
        up_lim = int(input('Upper boundary: '))
        print('')
    except:         # Reject if the data given are not integers
        print('Please retry. Make sure you input an integer.')
        continue
    
    if up_lim - low_lim <= 1:   # Reject if the lower boundary is larger than upper boundary, or no integer exists in the open interval
        print('Please retry. Make sure that lower boundary is smaller than the upper boundary,')
        print('And more than one integer exists between the boundaries.')
        continue

    else:
        SecretNum = random.randint(low_lim + 1, up_lim - 1)     # Choosing the secret number 
        print(name +', I have already chosen an integer between ' + str(low_lim) + ' and ' + str(up_lim) + ', excluding the boundaries.')
        num_guess = 1

        while True:
            print('')
            print('If you\'d like to give up, enter \'Give up\'.')
            guess = input('Otherwise, please guess a number between ' + str(low_lim) + ' and ' + str(up_lim) + ': ')    # Ask for guess
            print('')
            if guess == 'Give up' or guess == 'Give up.' : 
                break # This is when the player gives up
            else:
                try:
                    guess = int(guess) # Check if the guess is an integer
                except:
                    print('Please enter a valid input.')
                    continue
            if guess <= low_lim or guess >= up_lim:
                print('Please input a value within the range.')     # Check if the guess is outside the range
                
            elif guess < SecretNum:
                print('Too low. Guess higher!')
                num_guess = num_guess + 1   # Guess is lower than answer
                low_lim = guess
            elif guess > SecretNum:
                print('Too high. Guess lower!')
                num_guess = num_guess + 1       # Guess is higher than answer
                up_lim = guess
            else:
                break  # This is when the player hits the correct number

        if guess == 'Give up' or guess == 'Give up.':
            print(name+', I am sorry to see you give up. The secret number I have is ' + str(SecretNum) + '.')      # Correct response
        else:
            print('Congrats, ' + name + '. You guessed the correct number in ' + str(num_guess) + ' valid attempts.')       # Give up

        if input('Try again? Enter anything to play again. Enter nothing to end.') == '':   # Ask if the player wants to continue
            sys.exit()
        print('')
