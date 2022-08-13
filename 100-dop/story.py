class StarWars():
    def __init__(self, boba_helm = 0, han_blaster = 0, vader_card = 0, vader_saber = 0, vader_helm = 0, ship = 0, collectable_counter = 0, done = False):
        self.done = done
        self.boba_helm = boba_helm
        self.collectable_counter = collectable_counter
        self.han_blaster = han_blaster
        self. vader_saber = vader_saber
        self.vader_helm = vader_helm
        self. vader_card = vader_card
        self. ship = ship
    
    def intro(self):
        print('''
  .               A long time ago in a galaxy far, far away...   .
           .                                                                .
             .               .    .          .              .   .         .
               _________________      ____         __________
 .       .    /                 |    /    \    .  |          \ 
     .       /    ______   _____| . /      \      |    ___    |     .     .
             \    \    |   |       /   /\   \     |   |___>   |
           .  \    \   |   |      /   /__\   \  . |         _/               .
 .     ________>    |  |   | .   /            \   |   |\    \_______    .
      |            /   |   |    /    ______    \  |   | \           |
      |___________/    |___|   /____/      \____\ |___|  \__________|    .
  .     ____    __  . _____   ____      .  __________   .  _________
       \    \  /  \  /    /  /    \       |          \    /         |      .
        \    \/    \/    /  /      \      |    ___    |  /    ______|  .
         \              /  /   /\   \ .   |   |___>   |  \    \ 
   .      \            /  /   /__\   \    |         _/.   \    \            +
           \    /\    /  /            \   |   |\    \______>    |   .
            \  /  \  /  /    ______    \  |   | \              /          .
 .       .   \/    \/  /____/      \____\ |___|  \____________/  
                               .                                        .
     .                           .         .               .                 .
        ''')
        answer = input('''Begin? ''')
        if answer == 'yes' or answer == 'Yes' or answer == 'YES' or answer == 'y' or answer == 'Y':
            self.home_screen()
        elif answer == 'no' or answer == 'No' or answer == 'NO' or answer == 'n' or answer == 'N':
            # print('pussy')
            # print('YOU STUCK-UP, HALF-WITTED, SCRUFFY-LOOKING NERF HERDER!')
            print('coward.')
            self.done = True
        else:
            print('''
invalid input.
Try Again
            ''')
            self.alt_intro()

    def alt_intro(self):
        answer = input('''Begin? ''')
        if answer == 'yes' or answer == 'Yes' or answer == 'YES' or answer == 'y' or answer == 'Y':
            self.home_screen()
        if answer == 'no' or answer == 'No' or answer == 'NO' or answer == 'n' or answer == 'N':
            # print('pussy')
            # print('YOU STUCK-UP, HALF-WITTED, SCRUFFY-LOOKING NERF HERDER!')
            print('coward.')
            self.done = True
        else:
            print('''
invalid input.
Try Again
            ''')
            self.alt_intro()

    def home_screen(self):
        print('''
                   .          .
 .          .                  .          .              .
       +.           _____  .        .        + .                    .
   .        .   ,-~"     "~-.                                +
              ,^ ___         ^. +                  .    .       .
             / .^   ^.         \         .      _ .
            Y  l  o  !          Y  .         
    .       l_ `.___.'        _,[                  +
            |^~"-----------""~ ^|       +    
  +       . !                   !     .           .
         .   \                 /               
              ^.             .^            .             +.
                "-.._____.,-" .                    .
         +           .                .   +                       .
  +          .             +                                  .
         .             .      .      
 _______________________________________________
| You are trapped on board the Death Star.      |
| will you choose to stay put and wait for help |
| or escape on your own?                        | 
|                                               | 
| 1. Wait                                       |
| 2. Escape                                     |
|_______________________________________________|
        ''')

        answer = int(input("Which will you choose? "))
        if answer == 1:
            print('ok, standby.')
            self.done = True
        if answer == 2:
            self.level_one()


    def level_one(self):
        print('''
_____________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||\ 
   / ||--_||_____||_--|| \ 
  (_(||)-| P123-45 |-(||)_)
 ____________________________
|      Prisoner Title        |
|       Jedi  Knight         |
|____________________________|
        ''')

        answer = int(input('''
 _______________________________________________
| How will you escape?                          |
| 1. Use the force to unlock the cell.          | 
| 2. Wait for routine prisoner checks at 08:00. |
| 3. Use brute force to escape.                 |
|_______________________________________________|
        '''))

        if answer == 1:
            self.level_two()
        if answer == 2:
            self.collectable_one()
        if answer == 3:
            print('''
 _______________________________________________
| YOU DIED!                                     |
| a Storm Trooper saw your attempt and shot you.|
|_______________________________________________|
            ''')
            self.done = True

    def collectable_one(self):
        print(''' 
           |~
           |.---.
          .'_____`. /\ 
          |~xxxxx~| ||
          |_  #  _| ||
     .------`-#-'-----.
    (___|\_________/|_.`.
     /  | _________ | | |
    /   |/   _|_   \| | |
   /   /X|  __|__  |/ `.|
  (  --< \/    _\//|_ |`.
  `.    ~----.-~=====,:=======
    ~-._____/___:__(``/| |
      |    |      XX|~ | |
       \__/======| /|  `.|
       |_\|\    /|/_|    )
       |_   \__/   _| .-'
       | \ .'||`. / |(_|
       |  ||.'`.||  |   )
       |  `'|  |`'  |  /
       |    |  |    |\/
''')
        answer = int(input('''
 _____________________________________________________________________
| Boba Fett is coming to check on you, what do you do?                |
| 1. Play dead. when he is close, knock him out and steal his helmet. |
| 2. Attack him as he opens the door.                                 |
|_____________________________________________________________________|
        '''))
        if answer == 1:
            self.boba_helm += 1
            self.collectable_counter += 1
            print('''
 __________________________
|                          |
| You found a collectable! |
|__________________________|
            ''')
            self.level_two()
        elif answer == 2:
            print('''
 ___________________________________________
| YOU DIED!                                 |
| sadly, you weren\'t Han, Boba shot first. |
|___________________________________________|
            ''')
            self.done = True

    def level_two(self):
        answer = int(input('''
 __________________________________________
| YOU ESCAPED!                             |
| as you exit the cell you have 3 options: |
| 1. Take a right.                         |
| 2. Go straight.                          |
|__________________________________________|
        '''))
        if answer == 1:
            print('''  
 _____________
|             |
|  YOU DIED!  |
|_____________|
            ''')
            self.done = True
        if answer == 2:
            self.level_three()

    def level_three(self):
        answer = int(input('''
 ________________________________________
| You run into a man and his pet wookie. |
| What do you do?                        | 
| 1. Stop and talk.                      |
| 2. Keep going.                         |
|________________________________________|
        '''))
        if answer == 1:
            self.collectable_two()
        if answer == 2:
            self.level_four()

    def collectable_two(self):
        answer = int(input('''
 _____________________________________________
| Han Solo: Hey kid, what\'re you doing here? |
|                                             |
| 1. Tell the truth.                          |
| 2. Lie.                                     |
|_____________________________________________|
        '''))

        if answer == 1:
            print('''
 _______________________________________________________________
| You: I'm a force sensitive...                                 |
| Han Solo: Force sensitive? I don't know what that is kid but  |
| hey you can't be running around without a blaster.            |
| Here, take mine.                                              |
|_______________________________________________________________|
|                            |
|  You found a collectable!  |
|____________________________|
            ''')
            self.collectable_counter += 1
            self.han_blaster += 1
            self.level_four()
            print('''
 __________________________
|                          |
| You found a collectable! |
|__________________________|
            ''')
        if answer == 2:
            print('''
 ____________________________________________________________________________
| You: I was caught running spice.                                           |
| Han Solo: You think we're stupid? You dont get locked                      |
| up on the death star for running spice.                                    |
| You: ...                                                                   |
| Han Solo: Listen kid, we dont have time for this, just stay out of our way.|
|____________________________________________________________________________|
            ''')
            self.level_four()

    def level_four(self):
        answer = int(input('''
 _______________________________
| You\'ve come to a crossroads. |
| 1. Go right.                  |
| 2. Go left.                   |
|_______________________________|
        '''))
        if answer == 1:
            print('''
_____________
|             |
|  YOU DIED!  |
|_____________|

            ''')
            self.done = True
        if answer == 2:
            self.level_five()

    def level_five(self):
        answer = int(input('''
 __________________________________________________________
| You\'ve come across a wanted poster for Han Solo and his |
| friends. The reward is a vintage Darth Vader Card.       |
| what do you do?                                          |
| 1. Turn them in.                                         |
| 2. Ignore it and keep going.                             |
|__________________________________________________________|
        '''))

        if answer == 1:
            self.vader_card += 1
            self.collectable_counter += 1
            print('You found a collectable!')
            self.level_six()
        if answer == 2:
            self.level_six()

    def level_six(self):
        answer = int(input('''
 ____________________________________
| You\'ve come to another crossroad. |
| 1. Go right.                       |
| 2. Go left.                        |
|____________________________________|
        '''))
        if answer == 1:
            self.level_seven()
        if answer == 2:
            print('''
 _____________
|             |
|  YOU DIED!  |
|_____________|

            ''')
            self.done = True


    def level_seven(self):
        answer = int(input('''
 _____________________________
| You made it to the hangar!  |
| which ship do you choose?   |
| 1. Millenium Falcon.        |
| 2. Vaders ship.             |
| 3. Slave One.               |
|_____________________________|
        '''))
        if answer == 1:
            self.falcon_credits()
            self.ship == 1
        if answer == 2:
            self.boss()
        if answer == 3:
            self.slave_one_credits()
            self.ship == 2

    def boss(self):
        print(''' 
                       .-.
                      |_:_|
                     /(_Y_)\ 
                    ( \/M\/ )
 '.               _.'-/'-'\-'._
   ':           _/.--'[[[[]'--.\_
     ':        /_'  : |::"| :  '.\ 
       ':     //   ./ |oUU| \.'  :\ 
         ':  _:'..' \_|___|_/ :   :|
           ':.  .'  |_[___]_|  :.':\ 
            [::\ |  :  | |  :   ; : \ 
             '-'   \/'.| |.' \  .;.' |
             |\_    \  '-'   :       |
             |  \    \ .:    :   |   |
             |   \    | '.   :    \  |
             /       \   :. .;       |
            /     |   |  :__/     :   \ 
           |  |   |    \:   | \   |   ||
          /    \  : :  |:   /  |__|   /|
          |     : : :_/_|  /'._\  '--|_\ 
          /___.-/_|-'   \  \ 
                         '-'
        ''')
        answer = int(input('''
             -- B O S S  F I G H T --
 _________________________
| 1. Run away.            |
| 2. Throw sand at him.   |
| 3. Say "Padme is ugly." |
|_________________________|
        '''))

        if answer == 1:
            print('''
 _____________________________________________________________________
| YOU DIED...                                                         |
| Darth Vader froze you with the force and stabbed you with his saber.|
|_____________________________________________________________________|
            ''')
            self.done = True
        if answer == 2:
            self.vader_saber += 1
            self.vader_helm += 1
            self.collectable_counter += 2
            self.ship == 3
            print('''
 _________________________________
| Darth Vader doesn\'t like sand. |
| You found two collectables.     |
|_________________________________|
            ''')
            self.boss_credits()

        if answer == 3:
            print('''
 _________________________
| YOU DIED...             |
| from being force choked.|
|_________________________|
            ''')
            self.done = True


    def boss_credits(self):
        answer = int(input('''
 _____________________________
| You Escaped the Death Star! |
|                             |
| 1. See Collectables.        |
| 2. See Ship.                |
| 3. Play again.              |
| 4. Exit.                    |
|_____________________________|
        '''))

        if answer == 1:
            if self.han_blaster >= 1:
                print('''
                                   __ 1      1 __        _.xxxxxx.
                   [xxxxxxxxxxxxxx|##|xxxxxxxx|##|xxxxxxXXXXXXXXX|
   ____            [XXXXXXXXXXXXXXXXXXXXX/.\||||||XXXXXXXXXXXXXXX|
  |::: `-------.-.__[=========---___/::::|::::::|::::||X O^XXXXXX|
  |::::::::::::|2|%%%%%%%%%%%%\::::::::::|::::::|::::||X /
  |::::,-------|_|~~~~~~~~~~~~~`---=====-------------':||  5
   ~~~~                       |===|:::::|::::::::|::====:\O
                              |===|:::::|:.----.:|:||::||:|
                              |=3=|::4::`'::::::`':||__||:|
                              |===|:::::::/  ))\:::`----':/
                              `===|::::::|  // //~`######b
                                  `--------=====/  ######B
                                                   `######b
                                                    #######b
                                                    #######B
                                                    `#######b
                                                     #######P
                                                     `#####B
            
                ''')
            if self.boba_helm >= 1:
                print('''
 ____
/___/
 |     _______
 |  ,-'       `-,
 | /             \ 
|`|   __/| |\__   |
|]|_______________|
| ||___       ___||
| |    `-. .-'    |
 \`-,    | |    ,-'
  |  \   | |   /  |
  |   \  | |  /   |
  |    | | | |    |
  |,_  | | | |  _,|
     `-|_|-|_|-'
                ''')
            if self.vader_card >= 1:
                print('''
   _________________________________
  |:::::::::::::;;::::::::::::::::::|
  |:::::::::::'~||~~~``:::::::::::::|
  |::::::::'   .':     o`:::::::::::|
  |:::::::' oo | |o  o    ::::::::::|
  |::::::: 8  .'.'    8 o  :::::::::|
  |::::::: 8  | |     8    :::::::::|
  |::::::: _._| |_,...8    :::::::::|
  |::::::'~--.   .--. `.   `::::::::|
  |:::::'     =8     ~  \ o ::::::::|
  |::::'       8._ 88.   \ o::::::::|
  |:::'   __. ,.ooo~~.    \ o`::::::|
  |:::   . -. 88`78o/:     \  `:::::|
  |::'     /. o o \ ::      \88`::::|   
  |:;     o|| 8 8 |d.        `8 `:::|
  |:.       - ^ ^ -'           `-`::|
  |::.                          .:::|
  |:::::.....           ::'     ``::|
  |::::::::-'`-        88          `|
  |:::::-'.          -       ::     |
  |:-~. . .                   :     |
  | .. .   ..:   o:8      88o       |
  |. .     :::   8:P     d888. . .  |
  |.   .   :88   88      888'  . .  |
  |   o8  d88P . 88   ' d88P   ..   |
  |  88P  888   d8P   ' 888         |
  |   8  d88P.'d:8  .- dP~ o8       |   
  |      888   888    d~ o888    LS |
  |_________________________________|
                ''')
            if self.vader_saber >= 1:
                print('''
               .-~|
              /   |
       =============
        |         |
        |         |
        |         |
        \---------/
         )-------(
         (-------)
         )-------(
         (-------)
         )-------(
         (-------)
         )-------(--+
        /---------\ |
        | | | | | | |
        | | | | | | |
        | | | | | | |
        | | | | | |-+
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        |_|_|_|_|_|
                ''')
            self.boss_credits()
        
        if answer == 2:
#             if self.ship == 1:
#                 print('''
#              _     _
#             /_|   |_\  
#            //||   ||\\
#           // ||   || \\
#          //  ||___||  \\
#         /     |   |     \    _
#        /    __|   |__    \  /_\ 
#       / .--~  |   |  ~--. \|   |
#      /.~ __\  |   |  /   ~.|   |
#     .~  `=='\ |   | /   _.-'.  |
#    /  /      \|   |/ .-~    _.-'
#   |           +---+  \  _.-~  |
#   `=----.____/  #  \____.----='
#    [::::::::|  (_)  |::::::::]
#   .=----~~~~~\     /~~~~~----=.
#   |          /`---'\          |
#    \  \     /       \     /  /
#     `.     /         \     .'
#       `.  /._________.\  .'
#         `--._________.--'   
#                 ''')
#             elif self.ship == 2:
#                 print('''
#                  ___
#              ,--'___`--,
#            ,'   / _ \   `,
#           /   _/ / \ \_   \ 
#          '-,-'\ /   \ /`-,-`
#  __.----==-|   |     |   |-==----.__
#  `---==|---|   |     |   |---|==---'
#          .-`-,/|     |\,-'-.
#          |    \ `---' /    |
#          `   \ \     / /   '
#           |   \| --- |/   |
#           `    |     |    '
#            |   |     |   |
#             \  `.   ,'  /
#              \  |   |  /
#               \ |   | /
#                \`. .'/
#                -o|_|o-
#                  (_)
#                 ''')
#             elif self.ship == 3:
                print('''
              _             _
             //             \\
            /'               `\ 
           /,'     ..-..     `.\ 
          /,'   .''     ``.   `.\ 
         /,'   :   .---.   :   `.\ 
        I I   :  .'\   /`.  :   I I
        I b__:   . .`~'. .   :__d I
        I p~~:   . `._.' .   :~~q I
        I I   :   ./   \.   :   I I
         \`.   :   `---'   :   ,'/
          \`.   `..     ..'   ,'/
           \`.     ``~''     ,'/
            \`               '/    
             \\             //
              ~             ~
                ''')
                self.boss_credits()


        if answer == 3:
            self.intro()

        if answer == 4:
            self.done = True   

    def falcon_credits(self):
        answer = int(input('''
 _____________________________
| You Escaped the Death Star! |
|                             |
| 1. See Collectables.        |
| 2. See Ship.                |
| 3. Play again.              |
| 4. Exit.                    |
|_____________________________|
        '''))

        if answer == 1:
            if self.han_blaster >= 1:
                print('''
                                   __ 1      1 __        _.xxxxxx.
                   [xxxxxxxxxxxxxx|##|xxxxxxxx|##|xxxxxxXXXXXXXXX|
   ____            [XXXXXXXXXXXXXXXXXXXXX/.\||||||XXXXXXXXXXXXXXX|
  |::: `-------.-.__[=========---___/::::|::::::|::::||X O^XXXXXX|
  |::::::::::::|2|%%%%%%%%%%%%\::::::::::|::::::|::::||X /
  |::::,-------|_|~~~~~~~~~~~~~`---=====-------------':||  5
   ~~~~                       |===|:::::|::::::::|::====:\O
                              |===|:::::|:.----.:|:||::||:|
                              |=3=|::4::`'::::::`':||__||:|
                              |===|:::::::/  ))\:::`----':/
                              `===|::::::|  // //~`######b
                                  `--------=====/  ######B
                                                   `######b
                                                    #######b
                                                    #######B
                                                    `#######b
                                                     #######P
                                                     `#####B
            
                ''')
            if self.boba_helm >= 1:
                print('''
 ____
/___/
 |     _______
 |  ,-'       `-,
 | /             \ 
|`|   __/| |\__   |
|]|_______________|
| ||___       ___||
| |    `-. .-'    |
 \`-,    | |    ,-'
  |  \   | |   /  |
  |   \  | |  /   |
  |    | | | |    |
  |,_  | | | |  _,|
     `-|_|-|_|-'
                ''')
            if self.vader_card >= 1:
                print('''
   _________________________________
  |:::::::::::::;;::::::::::::::::::|
  |:::::::::::'~||~~~``:::::::::::::|
  |::::::::'   .':     o`:::::::::::|
  |:::::::' oo | |o  o    ::::::::::|
  |::::::: 8  .'.'    8 o  :::::::::|
  |::::::: 8  | |     8    :::::::::|
  |::::::: _._| |_,...8    :::::::::|
  |::::::'~--.   .--. `.   `::::::::|
  |:::::'     =8     ~  \ o ::::::::|
  |::::'       8._ 88.   \ o::::::::|
  |:::'   __. ,.ooo~~.    \ o`::::::|
  |:::   . -. 88`78o/:     \  `:::::|
  |::'     /. o o \ ::      \88`::::|   
  |:;     o|| 8 8 |d.        `8 `:::|
  |:.       - ^ ^ -'           `-`::|
  |::.                          .:::|
  |:::::.....           ::'     ``::|
  |::::::::-'`-        88          `|
  |:::::-'.          -       ::     |
  |:-~. . .                   :     |
  | .. .   ..:   o:8      88o       |
  |. .     :::   8:P     d888. . .  |
  |.   .   :88   88      888'  . .  |
  |   o8  d88P . 88   ' d88P   ..   |
  |  88P  888   d8P   ' 888         |
  |   8  d88P.'d:8  .- dP~ o8       |   
  |      888   888    d~ o888    LS |
  |_________________________________|
                ''')
            if self.vader_saber >= 1:
                print('''
               .-~|
              /   |
       =============
        |         |
        |         |
        |         |
        \---------/
         )-------(
         (-------)
         )-------(
         (-------)
         )-------(
         (-------)
         )-------(--+
        /---------\ |
        | | | | | | |
        | | | | | | |
        | | | | | | |
        | | | | | |-+
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        |_|_|_|_|_|
                ''')
            self.falcon_credits()
        
        if answer == 2:
            # if self.ship == 1:
                print('''
             _     _
            /_|   |_\  
           //||   ||\\
          // ||   || \\
         //  ||___||  \\
        /     |   |     \    _
       /    __|   |__    \  /_\ 
      / .--~  |   |  ~--. \|   |
     /.~ __\  |   |  /   ~.|   |
    .~  `=='\ |   | /   _.-'.  |
   /  /      \|   |/ .-~    _.-'
  |           +---+  \  _.-~  |
  `=----.____/  #  \____.----='
   [::::::::|  (_)  |::::::::]
  .=----~~~~~\     /~~~~~----=.
  |          /`---'\          |
   \  \     /       \     /  /
    `.     /         \     .'
      `.  /._________.\  .'
        `--._________.--'   
                ''')
#             elif self.ship == 2:
#                 print('''
#                  ___
#              ,--'___`--,
#            ,'   / _ \   `,
#           /   _/ / \ \_   \ 
#          '-,-'\ /   \ /`-,-`
#  __.----==-|   |     |   |-==----.__
#  `---==|---|   |     |   |---|==---'
#          .-`-,/|     |\,-'-.
#          |    \ `---' /    |
#          `   \ \     / /   '
#           |   \| --- |/   |
#           `    |     |    '
#            |   |     |   |
#             \  `.   ,'  /
#              \  |   |  /
#               \ |   | /
#                \`. .'/
#                -o|_|o-
#                  (_)
#                 ''')
#             elif self.ship == 3:
#                 print('''
#               _             _
#              //             \\
#             /'               `\ 
#            /,'     ..-..     `.\ 
#           /,'   .''     ``.   `.\ 
#          /,'   :   .---.   :   `.\ 
#         I I   :  .'\   /`.  :   I I
#         I b__:   . .`~'. .   :__d I
#         I p~~:   . `._.' .   :~~q I
#         I I   :   ./   \.   :   I I
#          \`.   :   `---'   :   ,'/
#           \`.   `..     ..'   ,'/
#            \`.     ``~''     ,'/
#             \`               '/    
#              \\             //
#               ~             ~
#                 ''')
                self.falcon_credits()

        if answer == 3:
            self.intro()

        if answer == 4:
            self.done = True   

    def slave_one_credits(self):
        answer = int(input('''
 _____________________________
| You Escaped the Death Star! |
|                             |
| 1. See Collectables.        |
| 2. See Ship.                |
| 3. Play again.              |
| 4. Exit.                    |
|_____________________________|
        '''))

        if answer == 1:
            if self.han_blaster >= 1:
                print('''
                                   __ 1      1 __        _.xxxxxx.
                   [xxxxxxxxxxxxxx|##|xxxxxxxx|##|xxxxxxXXXXXXXXX|
   ____            [XXXXXXXXXXXXXXXXXXXXX/.\||||||XXXXXXXXXXXXXXX|
  |::: `-------.-.__[=========---___/::::|::::::|::::||X O^XXXXXX|
  |::::::::::::|2|%%%%%%%%%%%%\::::::::::|::::::|::::||X /
  |::::,-------|_|~~~~~~~~~~~~~`---=====-------------':||  5
   ~~~~                       |===|:::::|::::::::|::====:\O
                              |===|:::::|:.----.:|:||::||:|
                              |=3=|::4::`'::::::`':||__||:|
                              |===|:::::::/  ))\:::`----':/
                              `===|::::::|  // //~`######b
                                  `--------=====/  ######B
                                                   `######b
                                                    #######b
                                                    #######B
                                                    `#######b
                                                     #######P
                                                     `#####B
            
                ''')
            if self.boba_helm >= 1:
                print('''
 ____
/___/
 |     _______
 |  ,-'       `-,
 | /             \ 
|`|   __/| |\__   |
|]|_______________|
| ||___       ___||
| |    `-. .-'    |
 \`-,    | |    ,-'
  |  \   | |   /  |
  |   \  | |  /   |
  |    | | | |    |
  |,_  | | | |  _,|
     `-|_|-|_|-'
                ''')
            if self.vader_card >= 1:
                print('''
   _________________________________
  |:::::::::::::;;::::::::::::::::::|
  |:::::::::::'~||~~~``:::::::::::::|
  |::::::::'   .':     o`:::::::::::|
  |:::::::' oo | |o  o    ::::::::::|
  |::::::: 8  .'.'    8 o  :::::::::|
  |::::::: 8  | |     8    :::::::::|
  |::::::: _._| |_,...8    :::::::::|
  |::::::'~--.   .--. `.   `::::::::|
  |:::::'     =8     ~  \ o ::::::::|
  |::::'       8._ 88.   \ o::::::::|
  |:::'   __. ,.ooo~~.    \ o`::::::|
  |:::   . -. 88`78o/:     \  `:::::|
  |::'     /. o o \ ::      \88`::::|   
  |:;     o|| 8 8 |d.        `8 `:::|
  |:.       - ^ ^ -'           `-`::|
  |::.                          .:::|
  |:::::.....           ::'     ``::|
  |::::::::-'`-        88          `|
  |:::::-'.          -       ::     |
  |:-~. . .                   :     |
  | .. .   ..:   o:8      88o       |
  |. .     :::   8:P     d888. . .  |
  |.   .   :88   88      888'  . .  |
  |   o8  d88P . 88   ' d88P   ..   |
  |  88P  888   d8P   ' 888         |
  |   8  d88P.'d:8  .- dP~ o8       |   
  |      888   888    d~ o888    LS |
  |_________________________________|
                ''')
            if self.vader_saber >= 1:
                print('''
               .-~|
              /   |
       =============
        |         |
        |         |
        |         |
        \---------/
         )-------(
         (-------)
         )-------(
         (-------)
         )-------(
         (-------)
         )-------(--+
        /---------\ |
        | | | | | | |
        | | | | | | |
        | | | | | | |
        | | | | | |-+
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        | | | | | |
        |_|_|_|_|_|
                ''')
            self.slave_one_credits()
        
        if answer == 2:
#             if self.ship == 1:
#                 print('''
#              _     _
#             /_|   |_\  
#            //||   ||\\
#           // ||   || \\
#          //  ||___||  \\
#         /     |   |     \    _
#        /    __|   |__    \  /_\ 
#       / .--~  |   |  ~--. \|   |
#      /.~ __\  |   |  /   ~.|   |
#     .~  `=='\ |   | /   _.-'.  |
#    /  /      \|   |/ .-~    _.-'
#   |           +---+  \  _.-~  |
#   `=----.____/  #  \____.----='
#    [::::::::|  (_)  |::::::::]
#   .=----~~~~~\     /~~~~~----=.
#   |          /`---'\          |
#    \  \     /       \     /  /
#     `.     /         \     .'
#       `.  /._________.\  .'
#         `--._________.--'   
#                 ''')
#             elif self.ship == 2:
                print('''
                 ___
             ,--'___`--,
           ,'   / _ \   `,
          /   _/ / \ \_   \ 
         '-,-'\ /   \ /`-,-`
 __.----==-|   |     |   |-==----.__
 `---==|---|   |     |   |---|==---'
         .-`-,/|     |\,-'-.
         |    \ `---' /    |
         `   \ \     / /   '
          |   \| --- |/   |
          `    |     |    '
           |   |     |   |
            \  `.   ,'  /
             \  |   |  /
              \ |   | /
               \`. .'/
               -o|_|o-
                 (_)
                ''')
        #     elif self.ship == 3:
        #         print('''
        #       _             _
        #      //             \\
        #     /'               `\ 
        #    /,'     ..-..     `.\ 
        #   /,'   .''     ``.   `.\ 
        #  /,'   :   .---.   :   `.\ 
        # I I   :  .'\   /`.  :   I I
        # I b__:   . .`~'. .   :__d I
        # I p~~:   . `._.' .   :~~q I
        # I I   :   ./   \.   :   I I
        #  \`.   :   `---'   :   ,'/
        #   \`.   `..     ..'   ,'/
        #    \`.     ``~''     ,'/
        #     \`               '/    
        #      \\             //
        #       ~             ~
        #         ''')
                self.slave_one_credits()

        if answer == 3:
            self.intro()

        if answer == 4:
            self.done = True   


start = input("click any key to start.")
user = StarWars()

while user.done != True:
    user.intro()