print('''
      ,--"""",--.__,---[],-------._         
       ,"   __,'            \         \--""""""==;-
     ," _,-"  "/---.___     \       ___\   ,-'',"
    /,-'      / ;. ,.--'-.__\  _,-"" ,| `,'   /
   /``""""-._/,-|:\       []\,' ```-/:;-. `. /
             `  ;:::      ||       /:,;  `-.\
                =.,'__,---||-.____',.=
                =(:\_     ||__    ):)=
               ,"::::`----||::`--':::"._
             ,':::::::::::||::::::::::::'.
    .__     ;:::.-.:::::__||___:::::.-.:::\     __,
       """-;:::( O )::::>_|| _<::::( O )::::-"""
   =======;:::::`-`:::::::||':::::::`-`:::::\=======
    ,--"";:::_____________||______________::::""----.          , ,
         ; ::`._(    |    |||     |   )_,'::::\_,,,,,,,,,,____/,'_,
       ,;    :::`--._|____[]|_____|_.-'::::::::::::::::::::::::);_
      ;/ /      :::::::::,||,:::::::::::::::::::::::::::::::::::/
''')
print("Welcome to Treasure Island\nYour Mission is to find the Treasure")
Enter = input("Would you like to get on the boat(Y or N)")
if Enter == 'Y':
    print("You Have Arrived on the Island")
    print("You see a Cave at your left Side And a Cliff to your Right")
    Move = input("Go Right or Go Left(R or L)")
    if Move == 'R':
        print("You needed those wings before you walked off a Cliff")
        print("                   Game Over")
    elif Move == 'L':
        print("You Enter The Cave And See Monsters")
        print("You hear a wisper 'Dont Run Away(Run)'")
        Action = input("Sneak through or fight(S or F)")
        if Action == 'S':
            print("You were able to sneak through the monsters")
            Door = input("You arrive at a cross roads choose Middle(M) Left(L) Right(R)")
            if Door == 'M':
                print(" You Reach the treasure but its fake")
            elif Door == 'L':
                print(" You Reach the treasure but its Gay treasure")
            elif Door == 'R':
                print(" You Reach the treasure")
        elif Action == 'F':
            print("You were able to Fight the monsters but Eventually they get you")
        elif Action == 'Run' or Action == 'run':
            print("You try to Run but the monster Catch you and BUTT FUCK YOU ")
else:
    print("You Decided not to go, A wise decision!")



