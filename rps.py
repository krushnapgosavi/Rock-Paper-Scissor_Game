import random
print("Hi , Friends .This is a game of rock-paper-scissor.Which is a popular game.\nSo let's begin the game")
print("Use this shortcuts :\n\t1)Rock-r\n\t2)Paper-p\n\t3)Scissor-s")

c=[]
def gme(x,y):
    #x=user  y=cpu
    if x == 'r' and y == 's':
        print('You win!!')
        c.append("Win")
        if False:
            continue
    elif x == 'r' and y =='p':
        print('You lose!!')
        c.append("Lose")
        if False:
            continue
    elif x == 'p' and y == 'r':
        print('You win!!')
        c.append("Win")
        if False:
            continue
    elif x == 'p' and y == 's':
        print('You lose!!')
        c.append("Lose")
        if False:
            continue
    elif x == 's' and y == 'r':
        print('You lose!!')
        c.append("Lose")
        if False:
            continue
    elif x == 's' and y == 'p':
        print('You win!!')
        c.append("Win")
        if False:
            continue
    elif x==y:
        print("It is a tie !!")
        c.append("Tie")
    else:
        print('You choose wrong choice!!')

ch = 1
while ch == 1:
    for i in range(1,6):
         a = input('Your choice : ')
         b = ['r','p','s']
         g = b[random.randint(0,2)]
         gme(a,g)
         print("CPUs'choice : "+ str(g))
    d = c.count("Win")
    e = c.count("Lose")
    f = c.count("Tie")
    if d > e:
        print("\nYou win " + str(d) + " times\n\nCongratulations !!")
    elif d < e:
        print("\nOverall You lose !!")
    elif d == e:
        print("It's a Tie")
    ch = int(input('Thanks for playing .Do you want to play again ??(Yes(1),No(0)) : '))

