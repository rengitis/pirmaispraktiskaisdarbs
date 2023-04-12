class Node(object):
    def __init__(self, depth, player, remaining, value = None):
        self.depth = depth # cik dziļu esam kokā (ar katru iteraciju samzinās līdz esam nonākuši sākumā)
        self.player = player # Poz vai Neg atkarīgs no tā kuram gājiens
        self.remaining = remaining # Atlikušais skaitlis
        self.value = value # Vērtība, kas katrai virsotnei piešķirta (+1, -1)
        self.children = [] # list priekš bērniem
        self.CreateChildren() # izveido bērnus
    def CreateChildren(self):
        if self.depth >= 0: # pārbauda vai dzilums ir 0, lai palīdzētu apstādīnāt koka veidošanu, kad esam nonākuši sākumā
            for i in range(1, 4): # cik daudz atņems (-1, -2, -3)/ izveido 3 bērnus
                v = self.remaining - i # v = tur atlikušo vērību
                self.children.append(Node(self.depth - 1, -self.player, v, self.RealVal(v)))
                # uztaisa jaunu bērnu un pievieno listam, tiks veidoti lidz depth bus vienads ar 0
    def RealVal(self, value): #nosaka veribu -1 vai +1
        if (value == 0):
            return 1 * self.player
        else:
            return 0

#Algoritms
def MinMax(node, depth, player):
    if (depth == 0) or (abs(node.value) == 1):
        return node.value

    BestValue = 1 * -player # pievieno pretējo vērtību kas nepieciešama uzvarai(sliktāko iznākumu)

    for i in range(len(node.children)): #itere cauri visiem berniem one by one
        child = node.children[i]
        val = MinMax(child, depth - 1, -player) # rekursīvi izpilda algoritmu ar bērniem, kas palīdz nonākt līdz koka apakšai
        if (abs(1 * player - val) < abs(1 * player - BestValue)): # meklē labāko iznākumu
            BestValue = val # ja izdodas atras labāku vērtību piešķir jauno vērību

    return BestValue
def MinMaxA(Rez, Turn):
    depth = 8 # piešķirtais dziļums cik tālu spēles koks ies
    node = Node(depth, Turn, Rez) # tiek izveidots koks ar ko algoritms strādās
    bestChoice = None # verība, kas saglabās to cik dators vēlas ņemt
    BestValue = -Turn * 1 # sak ar to veribu kuru dators negib
    for i in range(len(node.children)):  # iterē cauri bērniem
        child = node.children[i]
        val = MinMax(child, depth, -Turn) # iterē cauri algoritmam
        if (abs(Turn * 1 - val) <= abs(Turn * 1 - BestValue)):
            BestValue = val # ja atrodas labāka vērtība tad piešķir to
            bestChoice = i + 1# pārveido pareizajā vērībā, lai datoram nav iespēja ņemt 0

    print(str(Rez))
    print("Ai Izvelejas " + str(bestChoice) + " Ar virsotnes vertibu " + str(BestValue))
    Rez -= bestChoice
    print(str(Rez))
    # Debugs, lai spētu pamanīt ko dators ir izvēlējies un kāda vērība ir virsotnei
    return bestChoice