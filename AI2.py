from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer
from simpleai.search import SearchProblem, astar, breadth_first, depth_first, limited_depth_first, iterative_limited_depth_first, uniform_cost, greedy  
from AI1 import NQueens
import time


# base classtan child class oluşturmak için base class ı parametre olarak child classa verdik.

class NQueensProblem(SearchProblem): 
    
    def __init__(self,N):
        self.N = N
        self.problem = NQueens(N)
        self.initial = self.problem.state
        super(NQueensProblem, self).__init__(initial_state = self.initial)

    def string_to_int_list(self,string):
        rows=[]
        rows[:0]=string
        for i in range(len(rows)):
            rows[i]=int(rows[i])
        return rows
    
    def list_to_string(self,list2):
        string=""
        for i in range(len(list2)):
            list2[i]=str(list2[i])
            string=string+list2[i]
        return string

    def actions(self, state):
        actions_=[]
        k=0
        for i in range(self.N):
            array = [0 for i in range(self.N)]
            array[k]=1
            actions_.append(tuple(array))
            array = [0 for i in range(self.N)]
            array[k]=(-1)
            actions_.append(tuple(array))
            k+=1
        return actions_
        
    def board(self, state):#this function puts the queens on board according to given state
        N = self.N
        
        board = [[0 for satir in range(N)] for sutun in range(N)] 
        i=0
        for j in state :
            k=(N-int(j))
            board[k][i] = 1
            i+=1
        return board
    
    def is_goal(self, state):
        self.board(state)
        print(self.count_attacking_pairs(state))
        if(self.count_attacking_pairs(state) == 0):
            goal=True
        else:
            goal=False
        return goal
    
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
    
    def result(self, state, action):
        k=0
        rows = self.string_to_int_list(state)
        for i in action:
            rows[k]+=i
            k+=1
        result_ = self.list_to_string(rows)
        if self._is_valid(result_):
            state = result_
            return state
        else:
            return state
    def heuristic(self, state):
        h=self.count_attacking_pairs(state)
        return h
       
myViewer=ConsoleViewer()

p=NQueensProblem(5) 
start=time.time()

result = breadth_first(p, graph_search = True, viewer=myViewer)
end=time.time()

print(result.path())
print("\n")
print(result.state)
print("\n")
print(result.cost)
print("\n")
print(myViewer.stats)
print("time taken     = " ,end-start)

#astar, breadth_first, depth_first, limited_depth_first, 
#iterative_limited_depth_first, uniform_cost, greedy  