print("Welcome to the Forest Treasure Hunt!!!!")
print('''  __                    _   
 / _|                  | |  
| |_ ___  _ __ ___  ___| |_ 
|  _/ _ \| '__/ _ \/ __| __|
| || (_) | | |  __/\__ \ |_ 
|_| \___/|_|  \___||___/\__|
                            ''')
print('''You find yourself standing at the entrance of a dense forest, surrounded by towering trees and the sound of chirping birds.
The treasure map in your possession shows a marked spot deep within the forest.
Your adventure begins now!''')
input("Are you ready:")
print('''What would you like to do?
1=Explore the path ahead
2=Look for any clues around you''')
choose = int(input("1 or 2: "))
if choose == 1:
    print(''' 
                                                ,w.
                                              ,YWMMw  ,M  ,
                         _.---.._   __..---._.'MMMMMw,wMWmW,
                    _.-""        """           YP"WMMMMMMMMMb,
                 .-' __.'                   .'     MMMMW^WMMMM;
     _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
  ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
 ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
 WMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
 "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
            /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
           /  .'             /  (       .'  /     Ww._     `.  `"
          /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
 fsc     (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
          `"""                    `"""   `"'                  `---" ''')
    print("A lion is hiding on the way ahead. It will attack you.")
    print("You are out!!!")
elif choose == 2:
    print('''You start searching the area around you and notice an old tree with peculiar carvings.
    As you examine it closely, you realize the carvings resemble a set of symbols.''')
    print('''                           888             888 
                             888             888 
                             888             888 
.d8888b 888  88888888b.d88b. 88888b.  .d88b. 888 
88K     888  888888 "888 "88b888 "88bd88""88b888 
"Y8888b.888  888888  888  888888  888888  888888 
     X88Y88b 888888  888  888888 d88PY88..88P888 
 88888P' "Y88888888  888  88888888P"  "Y88P" 888 
             888                                 
        Y8b d88P                                 
         "Y88P"                                  ''')
    print('''What would you like to do?

1=Decode the symbols
2=Continue exploring the forest
3=Investigate the nearby river''')
    choice = int(input("1 or 2 or 3: "))
    if choice == 2:
        print("While exploring the forest, a lion is hiding on the way ahead. It will attack you.")
        print("You are out!!!")
    elif choice == 3:
        print('''There is a shark. It will attack you.
        You are out.''')
    elif choice == 1:
        print('''   _____________            __________
        /\            \_____ _   (\ -=-     \
        |;             _____|_|   `\  --=-=  \
        \/____________/             \ -==--=- \
                      __      ) -==-==- )
         jgs                  \/     ( =-==-=  (
                              \ -=-     \
                             /_)    -=-  )
                             `""""""""""`''')
        print('''You spend some time deciphering the symbols and manage to translate them into a message:
        "The key lies beneath the guardian of the ancient ruins."''')
        print('''What would you like to do?

1=Head towards the ancient ruins
2=Explore a different area of the forest
3=Investigate the nearby river''')
        choose = int(input("1 or 2 or 3: "))
        if choose == 2:
            print("While exploring the forest, a lion is hiding on the way ahead. It will attack you.")
            print("You are out!!!")
        elif choose == 3:
            print('''              (`.
                 \ `.
                  )  `._..---._
\`.       __...---`         o  )
 \ `._,--'           ,    ___,'
  ) ,-._          \  )   _,-'
 /,'    ``--.._____\/--''
''')
            print('''There is a shark. It will attack you.
            You are out.''')
        elif choose == 1:
            print('''You follow a winding path that leads you to a set of overgrown ancient ruins.
            The entrance is guarded by a massive stone statue.
            What would you like to do?''')
            print('''1=Look for a way to bypass the statue
            2=Solve a riddle to gain entrance
            3=Investigate a hidden passage nearby''')
            ans = input("1 or 2 or 3: ")
            if ans == '1':
                print("You are out.")
            elif ans == '3':
                print("You are out.")
            elif ans == '2':
                print('''The statue's inscription poses a riddle:
                I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?''')
                riddle = input("What's your answer?").lower()
                if riddle == 'echo':
                    print("As you utter the word echo, the statue's eyes glow briefly, and it steps aside, revealing a hidden entrance to the ruins.")
                    print('''You enter the ruins and explore the chambers, carefully searching for any signs of the treasure.
                    In one room, you discover a chest hidden beneath a pile of rubble.
                    What would you like to do?''')
                    chest = input('''
                    a=Open the chest
                    b=Investigate the surrounding area further
                    c=Return to the forest and explore a different area
                    ''')
                    if chest == 'b':
                        print("You are out.")
                    elif chest == 'c':
                        print("You are out.")
                    elif chest == 'a':
                        print('''You open the chest and find it filled with sparkling jewels and ancient artifacts.
                        Congratulations, you've found the treasure!''')
