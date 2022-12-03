import random
import os
clear = lambda: os.system('cls')
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
game = False
while game == False:
    comp = []
    user = []
    n=2
    while n>0:
        x = random.choice(cards)
        y = random.choice(cards)
        user.append(x)
        comp.append(y)
        n-=1

    print(f"computer:{comp[0]}")
    print(f"user:{user}")
    n1=len(user)
    n2=len(comp)
    z1=0
    z2=0
    
    while n2>0:
        z2+=comp[n2-1]
        if z2>21:
            for i in comp:
                if i == 11:
                    i = 1
            print("Computer's BUST user wins")
            game = True
            break
        if z2 == 21:
            print("Blackjack computer wins")
            game = True
            break
        n2-=1    
    print(z2)
    
    if game != True:
        while n1>0:
            z1+=user[n1-1]
            if z1>21:
                for i in user:
                    if i == 11:
                        z1-=10
            if z1 > 21:         
                print("User's BUST computer wins")
                game = True
                break
            if z1 == 21 and z2 != 21:
                print("Blackjack user wins")
                game = True
                break
            print(f"user:{user}")
            n1-=1
            
    while z1 < 21:
        k=input("Would you like to draw once more? Enter 'y' to draw or 'x' to exit\n")
        if k == "y":
            x = random.choice(cards)
            user.append(x)
            print(user)
            l=len(user)
            z1+=user[l-1]
            if z1>21:
                for i in user:
                    if i == 11:
                        z1-=10
            if z1>21:            
                print("User's BUST computer wins")
                game = True
                break
            if z1 == 21 and z2 != 21:
                print("Blackjack user wins")
                game = True
                break
        elif k == "x":
            break
    n2=1            
    if game != True:    
        while n2>0:
            y = random.choice(cards)
            comp.append(y)
            t=len(comp)
            z2+=comp[t-1]
            if z2>21:
                for i in comp:
                    if i == 11:
                        i = 1
                print("Computer's BUST user wins")
                game = True
                break
            if z2 == 21:
                print("Blackjack computer wins")
                game = True
                break
            if z2 <= 16 and n2 == 1:
                n2+=1
            n2-=1
    
    print(z2)
    if game != True:
        if z1<21 and z2<21:
            if z1<z2:
                print("computer wins")
                game = True
            elif z1==z2:
                print("its a draw")
                game = True
            else:
                print("user wins")
                game = True
    if game == True:
        print(f"user:{user}")
        print(f"computer:{comp}")
        again = input("Would you like to play again? (y/n):\n")
        if again == "y":
            clear()
            game = False
