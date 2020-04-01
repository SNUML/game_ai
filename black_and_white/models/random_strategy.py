import random as rd

class Player:
    def __init__(self) :
        pass

    def query(self, state) :
        return state.rem[rd.randrange(0,len(state.rem))]