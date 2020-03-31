def init() :
    pass

# output current state and use user input
def query(state) :
    for _ in range(10) : print()
    print("#" * 80)
    print(" {} ".format(state.name).center(80,'#'))
    print(" {}th stage ".format(state.stage).center(80,'#'))
    print("#" * 80)
    if state.stage != 1 :
        print()
        if state.res == 1 : print("Last result : win")
        elif state.res == 0 : print("Last result : draw")
        else : print("Last result : lose")
    if state.opp == -1 :
        print()
        print("You're in first turn!")
    else :
        print()
        print("You're in second turn!")
        print()
        if state.opp == 1 : print("Opponent drew White tile")
        else : print("Opponent drew Black tile")

    print()
    print("Opponent's tile remaining : {} white tile(s), {} black tile(s)".format(state.white,state.black))

    print()
    print("What you have : ",end='')
    for num in state.rem :
        print(("W" if num % 2 == 1 else "B")+str(num),end=' ')
    print()

    print()
    for _ in range(4) : print("#" * 80)
    print()
    return int(input("your choice : "))