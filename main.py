import random


cond=True
while cond:
    num=random.randint(1,100)

    print("""Welcome to the Number Guessing game !
The computer has randomly chosen a number between 1 to 100
You have to guess the number in given number of attempts
Do you want to play 'easy' or 'hard' level ?
Enter 'easy' for 'easy' level
Enter 'hard' for 'hard' level""")
    choice=input()
    if choice=="easy":
        n=10
    else:
        n=5
    for i in range(n):
        print(f'You have {n-i} attempts remaining' )
        guess=int(input('Enter your guess number '))
        if guess==num:
            print('You have entered the correct number, you have won')
            break
        elif guess<num:
            print('The number entered is lower than actual number, try again !')
        elif guess>num:
            print('The number entered is higher than actual number, try again !')
    print('The actual number is',num)
    print("""
Do you want to play again ?
Enter 'yes' for yes and 'no' for no. """)
    val=input()
    if val=="yes":
        cond=True
    else:
        cond=False
print('The game ends')
    