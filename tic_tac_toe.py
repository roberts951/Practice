player1 = input("Player 1 Name:")
player2 = input("Player 2 Name:")
game_finished = False
player1_turn = True
field=[]

def define_field():
    global field
    global game_finished
    field=[0,1,2,3,4,5,6,7,8]
    game_finished = False

define_field()

def player_win_check(t):
    global game_finished
    if t == "X":
        print(player1,"Wins the game")

    if t == "O":
        print(player2,"Wins the game")

    game_finished = True

def win_check(t):
    if field[0] == t and field[1] == t and field[2] == t:
        player_win_check(t)

    elif field[0] == t and field[3] == t and field[6] == t:
        player_win_check(t)

    elif field[0] == t and field[4] == t and field[8] == t:
        player_win_check(t)

    elif field[2] == t and field[5] == t and field[8] == t:
        player_win_check(t)

    elif field[2] == t and field[4] == t and field[6] == t:
        player_win_check(t)

    elif field[8] == t and field[7] == t and field[6] == t:
        player_win_check(t)


def field_f():
    print(field[0],field[1],field[2])
    print(field[3],field[4],field[5])
    print(field[6],field[7],field[8])
    print("\n")

print("The following are the field coordinates: \n")
field_f()
print(" \n(If you would like to select top left field for your move, you would select \"0\") \n\nEnjoy! \n")

def move():
    global player1_turn
    if player1_turn == True:
        while True:
            try:
                move=int(input(player1+"'s turn:"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue

            if move < 0 or move > 8:
                print("Value must be between 0-8")
                continue
            if move != field[move]:
                print("Nice try, but the field is already taken")
                continue
            else:
                break
        print("\n")
        field[move]="X"
        field_f()
        win_check_value="X"
        win_check(win_check_value)
        player1_turn = False

    elif player1_turn == False:
        while True:
            try:
                move=int(input(player2+"'s turn:"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue

            if move < 0 or move > 8:
                print("Value must be between 0-8")
                continue
            if move != field[move]:
                print("Nice try, but the field is already taken")
                continue
            else:
                break
        field[move]="O"
        field_f()
        win_check_value="O"
        win_check(win_check_value)
        player1_turn = True

while True:
    if game_finished == False:
        move()
    else:
        try:
            choice=input("Restart Game? y/n")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if choice=="y":
            print("Resetting field")
            define_field()
            continue
        if choice=="n":
            print("Quitting...")
            quit()
        if choice not in ("n","y"):
            print("Type either 'n' or 'y' ")
            continue