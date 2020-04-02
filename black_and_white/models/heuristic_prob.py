import random as rd
class Player:
    def __init__(self):
        self.prob_table = [1]*10
        self.possible_black = [[0, 2, 4, 6, 8]]  # every possible combinations
        self.possible_white = [[1, 3, 5, 7, 9]]
        self.last_pick = -1
        pass

    def query(self, state):
        if state.last_opp == 0:
            self.update_possible_list(self.possible_black, self.last_pick, state.res, 0)
        else:
            self.update_possible_list(self.possible_white, self.last_pick, state.res, 1)
        #print("white: ",self.possible_white)
        #print("black: ",self.possible_black)
        self.update_prob_table(self.possible_black, 0)
        self.update_prob_table(self.possible_white, 1)
        self.last_pick = self.heuristic_query2(state.opp, state.rem)
        print(self.last_pick)
        return self.last_pick

    def update_possible_list(self, pos_list, last_pick, res, color):
        if last_pick < 0:
            return
        #print("pos_list: ",pos_list)
        new_list = []
        for comb in pos_list:
            for num in comb:
                if ((res > 0) & (num < last_pick)) | ((res < 0) & (num > last_pick)) | ((res == 0) & (num == last_pick)):
                    new_comb = comb.copy()
                    new_comb.remove(num)
                    if len(new_comb) == 0:
                        continue
                    new_list.append(new_comb)
        #print("new_list: ",new_list)
        #print("color: ",color)
        if color == 0:
            self.possible_black = new_list
        else:
            self.possible_white = new_list
        return new_list

    def update_prob_table(self, pos_list, color):
        for i in range(color,10,2):
            self.prob_table[i]=0
        for comb in pos_list:
            for num in comb:
                self.prob_table[num]+=1
        if len(pos_list) > 0:
            for i in range(color,10,2):
                self.prob_table[i]/=len(pos_list)
        #print("prob_table: ",self.prob_table)
        

    def heuristic_query(self, opp, rem):
        value_table = [0]*10
        sum = 0
        if opp > 0:
            for i in range(opp,10,2):
                self.prob_table[i] = 0

        for i in range(0,10):
            value_table[i] = (2*sum+self.prob_table[i])/pow(i+1,1)
            sum += self.prob_table[i]

        print("value table: ",value_table)
        maxi = -1e9
        for n in rem:
            if value_table[n] >= maxi:
                maxi = value_table[n]
        rand_list = []
        for n in rem:
            if value_table[n] == maxi:
                rand_list.append(n)
        return rand_list[rd.randrange(0,len(rand_list))]

    def heuristic_query2(self, opp, rem):
        value_table = [0]*10
        sum = 0
        if opp > 0:
            for i in range(opp,10,2):
                self.prob_table[i] = 0

        maxi = -1e9
        for n in rem:
            for i in range(0,10):
                if n > i:
                    value_table[n] += (self.prob_table[i])*(5-n+i)
                elif n < i:
                    value_table[n] += (self.prob_table[i])*(-5+i-n)
            if value_table[n] >= maxi:
                maxi = value_table[n]

        #print(value_table)
        rand_list = []
        for n in rem:
            if value_table[n] == maxi:
                rand_list.append(n)
        return rand_list[rd.randrange(0,len(rand_list))]