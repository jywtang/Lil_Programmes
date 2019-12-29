def collatz(number):
    if number%2 == 0:
        number = number//2
    else:
        number = 3*number +1
    print(number)
    return number
    
print('Input a positive integer to start the Collatz sequence: ')
while True:
    try:    # Check if input is an integer
        number = int(input())   
    except:     # Otherwise, reject and restart
        print('\nPlease enter a positive integer')
        continue
    if number <= 0:
        print('\nPlease enter a positive integer')
        continue
    while True:     # Start sequence
        number = collatz(number)
        if number == 1:
            break   # End sequence when it reaches 1
    print('\nType another positive integer to start again')
