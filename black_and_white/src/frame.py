class PlayerVisibleState :
    def __init__(self,rem,oppw,oppb,oppl,lopp,res,score,hist,name) :
        self.rem = rem # my remaining tiles in list
        self.white = oppw # opponent white tile remaining (includes self.opp)
        self.black = oppb # opponent black tile remaining (includes self.opp)
        self.opp = oppl # what opponent drew : black - 0, white - 1, you're first turn - -1
        self.last_opp = lopp # what oppenent drew in a last turn : black - 0, white - 1 
        self.res = res # result of last round : win - 1, lose - -1, draw - 0
        self.stage = 10 - len(rem) # current round
        self.score = score # current score
        self.history = hist # list of (my tile, opp tile color, result)
        self.name = name # Player1 or Player2

class State :
    def __init__(self) :
        self.rem = [list(range(9)), list(range(9))]
        self.score = [0,0]
        self.turn = 0
        self.last = 0
        self.lopp = [-1,-1]
        self.history = []
    
    def draw(self, c1, c2) :
        if not c1 in self.rem[0] :
            raise Exception("Player 1 drew invalid tile : {} not in list".format(c1))
        if not c2 in self.rem[1] :
            raise Exception("Player 2 drew invalid tile : {} not in list".format(c2))
        self.history.append((c1,c2))
        self.rem[0].remove(c1)
        self.rem[1].remove(c2)
        self.lopp = [c2%2, c1%2]
        if c1 > c2 :
            self.turn = 0
            self.last = -1
            self.score[0] += 1
        elif c1 < c2 :
            self.turn = 1
            self.last = 1
            self.score[1] += 1
        else :
            self.last = 0
    
    def player_states(self) :
        def res(a,b) :
            if a>b:return 1
            elif a<b:return -1
            return 0
        w2 = sum(map(lambda x : x%2==1, self.rem[1]))
        b2 = len(self.rem[1])-w2
        his1 = map(lambda p : (p[0],p[1]%2,res(p[0],p[1])),self.history)
        ps1 = PlayerVisibleState(self.rem[0],w2,b2,-1,self.lopp[0],-self.last,self.score,his1,"Player1")
        w1 = sum(map(lambda x : x%2==1, self.rem[0]))
        b1 = len(self.rem[0])-w1
        ps2 = PlayerVisibleState(self.rem[1],w1,b1,-1,self.lopp[1],self.last,self.score,\
                    map(lambda p : (p[1],p[0]%2,res(p[1],p[0])),self.history),"Player2")
        return (ps1,ps2)

