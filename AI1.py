import random

#class definition for NQueens
class NQueens():
    """ class constructor
    initializes the instance attributes N and state """
    def __init__(self, N):
        self.N = N
        self.state = self.set_state()
     

    """ returns a formatted string
    that represents the instance """        
    def __str__(self):
        
        return 'N : ' + str(self.N) + ' \nstate : ' + str(self.state)
        

    """ Sets the instance attribute state by displaying 
    a menu to the user. The user either enters the state 
    manually or prompts the system to generate a random state.
    Check if the input state is a valid state. """         
    def set_state(self):
        choice = int (input("How do you want to set state?\n 1. Set state manually\n 2. Set state randomly\n"))
        if(choice == 1):
            state = input("Enter State: ")
            while(self._is_valid(state) == False):
                choice = int (input("Enter a valid state!\nHow do you want to set state?\n 1. Set state manually\n 2. Set state randomly\n"))
                state = input("Enter State: ")
        else:
            state = self.generate_random_state()
        return state

    """ generates and returns a valid random state """
    def generate_random_state(self):
        state = ""
        for i in range(self.N):
            state = state + str(random.randint(1,self.N))
        return state
        

    
    """ This is an internal function that takes a state_str as input
    and return if this is a valid state or not """
    def _is_valid(self,state_str):
        validation = True
        if not state_str.isdigit():
            validation=False
            
            
        elif len(state_str)!=self.N:
            validation=False
            
            
        elif state_str.__contains__('0'):
            validation=False
            
                
        for i in state_str:
            if ((int(i)>self.N) or (int(i)<1)):
                validation = False
                break
                        
        return validation
        
        
        

    """ This is the primary function of this class.
    It returns the number of attacking pairs in the board.
    """  
    def board(self, state):#this function puts the queens on board according to given state
        N = self.N
        state=self.state
        board = [[0 for satir in range(N)] for sutun in range(N)] 
        i=0
        for j in state :# j=1, j=3, j=4, j=5, j=5
            k=(N-int(j))
            board[k][i] = 1
            i+=1
        return board
        #(dizinin elemanları olan dizilerin alt alta yazdığını düşünürsek kağıttaki çizimle aynı şekilde gözükecektir.)
        
    def count_attacking_pairs(self, instate):
        self.instate = instate
        N = self.N
        board = self.board(instate)
        
        #bazı gerekli fonksiyonlar:
        def factorial(sayi):
            deger=1
            for i in range(sayi):
                deger=deger*(i+1)
            return deger

        def combination(sayi1,sayi2):
            comb = factorial(sayi1)/(factorial(sayi2)*factorial(sayi1-sayi2))   
            return int(comb)

        #------------------------------------------------------------------------------------------------
        #satirları kontrol etme kısmı:
        def rows():
            numPairs=0 #attack eden pairların sayısı
            count=0
            #sutun=0
            for satir in range (N):
                for sutun in range(N):
                    queen = board[satir][sutun]
                    count+=queen
                if count>1:
                    numPairs = numPairs + combination(count,2)
                count=0
            return int(numPairs)


        #------------------------------------------------------------------------------------------------
        #çapraz kontrol kısmı:
        # alt left diagonal (6-11. left diagonals, includes 6):
        def leftDiago1():
            numPairs=0 #attack eden pairların sayısı
            count=0
            n=N
            for i in range(N):
                sutun = i
                satir = N-1
                for j in range(n):
                    queen = board[satir][sutun]
                    count+=queen
                    satir = satir-1
                    sutun = sutun+1
                n=n-1
                if count>1:
                    numPairs = numPairs + combination(count,2)
                count=0
            return int(numPairs)

        # üst left diagonal (1-6. left diagonals, doesn't include 6)
        def leftDiago2():
            numPairs=0 #attack eden pairların sayısı
            count=0
            n=N-1
            for i in range(N-1):
                sutun = 0
                satir = n-1
                for j in range(n):
                    queen = board[satir][sutun]
                    count+=queen
                    satir = satir-1
                    sutun = sutun+1
                n=n-1
                if count>1:
                    numPairs = numPairs + combination(count,2)
                count=0
            return int(numPairs)

        # alt right diagonal (6-11. left diagonals, includes 6):
        def rightDiago1():
            numPairs=0 #attack eden pairların sayısı
            count=0
            n=N
            for i in range(N):
                sutun = (N-1)-i
                satir = N-1
                for j in range(n):
                    queen = board[satir][sutun]
                    count+=queen
                    satir = satir-1
                    sutun = sutun-1
                n=n-1
                if count>1:
                    numPairs = numPairs + combination(count,2)
                count=0
            return int(numPairs)

        # alt right diagonal (1-6. left diagonals, doesn't include 6):
        def rightDiago2():
            numPairs=0 #attack eden pairların sayısı
            count=0
            n=N-1
            for i in range(N-1):
                sutun = N-1
                satir = n-1
                for j in range(n):
                    queen = board[satir][sutun]
                    count+=queen
                    satir = satir-1
                    sutun = sutun-1
                n=n-1
                if count>1:
                    numPairs = numPairs + combination(count,2)
                count=0
            return int(numPairs)
        numpairs = rows() + leftDiago1() + leftDiago2() + rightDiago1() + rightDiago2()
        return numpairs
"""
problem=NQueens(4)

print(problem)

#print(problem.board(problem.state))
a = problem.count_attacking_pairs(problem.state)
print(a)
"""




