def intro():
    print("welcome to the lost jungle adventure!")
    print("you find yourself at the edge of a dark, mysterious forest. ")
    print("your goal is to find the hidden tresure and escape safely.\n")
    start_game()
    
def start_game():
    print("you see two paths ahead of you.")
    choice = input("do you want to go 'left' or 'right' ").lower().strip()
    
    if choice == "left":
        river_path()
    elif choice == "right":
        cave_path()
    else:
        print("invalid choice. please type 'left' or 'right'?")
        start_game()
def river_path():
    print("\n you walk left and arrive at a wide, fast_flowing river.")
    print("you see a old wooden boat, or yan can try to swim across.")
    choice = input("do you want to 'boat' or 'swim'?").lower().strip()
    
    if choice == "boat":
        print("\n congratulations! the boat safely takes you to the othe side.")
        print("you find thehidden golden tresure chest! you win!")
    elif choice == "swim":
        print("\n oh no! the river current was too strong. you got washed away.")
        print("game over!")
    else:
         print("invalid choice. try again.") 
         river_path()
def cave_path():
    print("\n you walk right and finda dark, creepy cave.")
    print("you  hear a strange noise from inside.")
    choice = input("do you want to 'enter' the cave or 'run' away?").lower().strip()
    
    if choice == "enter":
        print("\n inside the cave, you wake up a sleeping dragon!")
        print("the dragon breathes fire. game over!")
    elif choice == "run":
        print("\n you run back safely to the starting point.")
        start_game()
    else:
        print("invalid choice. try again.")
        cave_path()
intro()                                   
                   
    