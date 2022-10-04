import random
n = 20
to_be_quessed = int( n*random.random()  ) + 1
guess  = 0
while guess != to_be_quessed:
    guess = int(input('New Number : '))
    if guess > 0 :
        if guess > to_be_quessed:
            print('Number is to large')
        elif guess < to_be_quessed:
            print('Number is too small')
    else :
        print('Sorry that you\'re giving up!'  )
        break
else :
    print('Congratulation!!!! You made it!')
