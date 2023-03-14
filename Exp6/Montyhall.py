import random

win = 0
lose = 0
playing = True

while playing:

    door = [1,2,3]
    x = 0
    a = random.choice(door) 
    b = int(input("Please choose a door (1-3): ")) 
    if a == b:
      
        door.remove(a)
        x = random.choice(door)
        c = x
        print("You chose door {}".format(b))
        print("I choose door {}".format(c))

       
        door = [1,2,3]
        door.remove(x)
        door.remove(a)
        d = door[0]
        print("You're left with doors {} and {}".format(b,d))
        choice = input("Will you SWITCH to door {}? y/n: ".format(d)) 

        
        if choice == "y":
            print("Bad luck.  You lost.  You should have stuck as you already had the right answer.")
            lose += 1
        else:
            print("Huzzah! You made the right choice by STICKING!")
            win += 1
        print("{} wins and {} losses".format(win,lose))
    else:
        
        door.remove(a)
        door.remove(b)
        e = door[0]
        print("You chose door {}".format(b))
        print("I choose door {}".format(e))

       
        print("You're left with doors {} and {}".format(a,b))
        choice = input("Will you SWITCH to door {}? y/n: ".format(a)) 

        
        if choice == "y":
            print("HUZZAH!  YOU WIN")
            win +=1
        else:
            print("Bad luck.  You should have switched. You chose the wrong door at the start")
            lose += 1
        print("{} wins and {} losses".format(win,lose))

    ans = input("\nPress Enter to play again, 'q' to quit")
    if len(ans) > 0: playing = False
