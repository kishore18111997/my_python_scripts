n = 7

for chance in range (0,3):
    number = int(input('guess a number: '))

    if number == n:
        print ('yay you won...!')
        break

    else:
        print ('you lost better luck next time')
