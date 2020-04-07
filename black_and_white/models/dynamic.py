class Player:
    def __init__(self) :
        self.initialized = False
        pass

    def init(self) :
        if self.initialized :
            return
        self.initialized = True

        self.D = [0]*(6**9)
        self.via = [0]*(6**9)

        response = input("Load from precalcD.txt? (Y/n) ")
        if response == 'y' or response == 'Y' :
            with open("precalcD.txt","r") as f:
                s = f.readline()
                for bit in range(6**9) :
                    self.via[bit] = int(s[bit*3:bit*3+3])
            return
        calc_cnt = 1
        ts = 0.
        tc = 0
        for bit in range(6**9) :
            tmp = bit
            if bit == (6**9)*calc_cnt//100 :
                print("Initializing {}% Done...".format(calc_cnt))
                calc_cnt+=1
            rem = []
            blk = []
            wht = []
            dig = []
            for i in range(9) :
                dig.append(tmp%6)
                if tmp%6==0 :
                    blk.append(list(range((i+1)//2)))
                elif tmp%6==1 :
                    blk.append(list(range(i//2+1,5)))
                elif tmp%6==2 :
                    wht.append(list(range(i//2)))
                elif tmp%6==3 :
                    wht.append(list(range((i+1)//2,4)))
                elif tmp%6==4 :
                    if i%2==0 :
                        blk.append([i//2])
                    else :
                        wht.append([i//2])
                else :
                    rem.append(i)
                tmp = tmp//6
            if len(blk) > 5 or len(wht) > 4:
                continue
            if len(rem) == 0 :
                scv = [1,-1,1,-1,0,0]
                sco = sum(map(lambda v : scv[v],dig))
                if sco > 0 :
                    self.D[bit] = 1
                elif sco < 0 :
                    self.D[bit] = 0
                else :
                    self.D[bit] = 0.5
                continue
            blk.sort(key=(lambda l : len(l)))
            wht.sort(key=(lambda l : len(l)))
            def calcp(prob,blk,selected,idx) :
                if idx == len(blk) :
                    for i in range(len(prob)) :
                        if not selected[i] :
                            prob[i] += 1
                    return 1
                l = blk[idx]
                s = 0
                for v in l :
                    if not selected[v] :
                        selected[v] = True
                        s += calcp(prob,blk,selected,idx+1)
                        selected[v] = False
                return s
            prob = [0.]*5
            prow = [0.]*4
            sp = calcp(prob,blk,[False]*5,0)
            if sp == 0 : continue
            prob = [v/sp for v in prob]
            sp = calcp(prow,wht,[False]*4,0)
            if sp == 0 : continue
            prow = [v/sp for v in prow]
            rn = len(rem)
            pro = [0]*9
            for i in range(5) :
                pro[i*2] = prob[i]
                if i<4 : pro[i*2+1] = prow[i]
            maxi = maxiw = maxib = -1e9
            maxt = maxw = maxb = rem[0]
            def printb(bit) :
                tmp = bit
                for _ in range(9) :
                    print(tmp%6,end='')
                    tmp//=6
                print()
            #print("!!!!!!!!")
            #printb(bit)
            for r in rem :
                bwp = 0.
                blp = 0.
                wwp = 0.
                wlp = 0.
                bdp = 0.
                wdp = 0.
                for i in range(9) :
                    if i < r :
                        if i%2==0 : bwp += pro[i]/rn
                        else : wwp += pro[i]/rn
                    elif i > r :
                        if i%2==0 : blp += pro[i]/rn
                        else : wlp += pro[i]/rn
                    else :
                        if i%2==0 : bdp += pro[i]/rn
                        else : wdp += pro[i]/rn
                rp = (6**r)
                valb = (bwp*(self.D[bit+(0-5)*rp])+\
                    blp*(self.D[bit+(1-5)*rp])+\
                    bdp*(self.D[bit+(4-5)*rp])) / max(bwp+blp+bdp,1e-8)
                valw = (wwp*(self.D[bit+(2-5)*rp])+\
                    wlp*(self.D[bit+(3-5)*rp])+\
                    wdp*(self.D[bit+(4-5)*rp])) / max(wwp+wlp+wdp,1e-8)
                val = bwp*(self.D[bit+(0-5)*rp])+\
                    blp*(self.D[bit+(1-5)*rp])+\
                    wwp*(self.D[bit+(2-5)*rp])+\
                    wlp*(self.D[bit+(3-5)*rp])+\
                    (bdp+wdp)*self.D[bit+(4-5)*rp]
                #print(bwp,blp,wwp,wlp,dp)
                #print(self.D[bit+(0-5)*rp],self.D[bit+(1-5)*rp],self.D[bit+(2-5)*rp],self.D[bit+(3-5)*rp],self.D[bit+(4-5)*rp])
                #print("="+str(val))
                if maxi < val :
                    maxi=val
                    maxt=r
                if maxiw < valw :
                    maxiw=valw
                    maxw=r
                if maxib < valb :
                    maxib=valb
                    maxb=r
            #print("!!!!!!!!")
            self.D[bit] = maxi
            self.via[bit] = maxt*100+maxb*10+maxw
            ts += maxi
            tc += 1
            '''
            def cd(bit) :
                tmp = bit
                dc = 0
                dd = 0
                for _ in range(9) :
                    if tmp%6==4 : dc+=1
                    if tmp%6==5 : dd +=1
                    tmp//=6
                return (dc,dd)
            if tc % 10000 == 0:
                printb(bit)
                for i in range(9) :
                    print(str(pro[i]),end=' ')
                print()
                print("{} : {}, {}, average : {}".format(bit,maxi,maxt,ts/tc))
                '''
        
        with open("precalcD.txt","w") as f:
            for bit in range(6**9) :
                val = self.via[bit]
                f.write(str(val//100)+str(val//10%10)+str(val%10))

    # output current state and use user input
    def query(self, state) :
        bit = 0
        for p in state.history :
            my = p[0]
            opp = p[1]
            res = p[2]
            dig = 0
            if opp == 0:
                if res == 1: dig=0
                elif res == -1 : dig=1
                else : dig=4
            else :
                if res == 1: dig=2
                elif res==-1 : dig=3
                else : dig=4
            bit += (6**my)*dig
        for r in state.rem :
            bit += (6**r)*5
        dig = [self.via[bit]//100,self.via[bit]//10%10,self.via[bit]%10]
        return dig[state.opp+1]