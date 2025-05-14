def ai_number_guesser():

    name = input('Enter your name')

    print('Welcome to the guessing game', name)

    low = int(input('enter lowest value'))
    high = int(input('enter high value'))
    attempt = 0

    print('Type enter to begin')

    while True:
        low <= high
        guess = ((low + high) // 2)

        print('my guess is', guess)

        feedback = input('Enter h for higher \n l for lower \n c for correct')

        if feedback == 'c':
            print('yaa i guessed your number in ', attempt, 'and the number is ', guess)
            break
        elif feedback == 'h':
            low = guess + 1
        elif feedback == 'l':
            high = guess - 1
        else:
            print('Enter h for higher \n l for lower \n c for correct')

    if low > high:
        print('ar you playing by the rules properly?')
        
ai_number_guesser()
