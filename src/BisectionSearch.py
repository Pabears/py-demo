# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed
# correctly. l
# Game over. Your secret number was: 83
# Sorry, I did not understand your input.

i = 50
ll = 0
rl = 100
print('Please think of a number between 0 and 100!')
r = ''
while (r != 'c'):
    print('Is your secret number ', i, '?')
    r = input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed")
    if (r != 'h' and r != 'l' and r != 'c'):
        print('Sorry, I did not understand your input.')
    elif (r == 'c'):
        print('Game over. Your secret number was: ', i)
        break
    elif (r == 'h'):
        rl = i
        i = int(i - (i - ll) / 2)
    else:
        ll = i
        i = int(i + (rl - i) / 2)
