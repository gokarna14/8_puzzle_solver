from cmath import inf
import copy
import pygame


class Solver:
    def __init__(self, initialState, finalState):
        self.initial = initialState
        self.goal = finalState
        self.traversedState_ = []
        self.stack = []
        self.costStack = []
        self.minCost = inf
        self.solve(self.initial, self.goal)


    def cost(self, toCompareMat):
        result = 0
        for rowIndex in range(len(self.goal)):
            for columnIndex in range(len(self.goal[rowIndex])):
                if self.goal[rowIndex][columnIndex] != toCompareMat[rowIndex][columnIndex]:
                    (goalRowIndex, goalColumnIndex) = self.index_2d(self.goal, toCompareMat[rowIndex][columnIndex])
                    rowChange = abs(goalRowIndex - rowIndex)
                    columnChange = abs(goalColumnIndex - columnIndex)
                    result += rowChange + columnChange
        return result


    def print_matrix(self, mat, sep = ' '):
        a = [i for i in mat]
        
        while(len(a)<10):
            a.append([
                [' ', ' ', ' '],
                [' ', ' ', ' '],
                [' ', ' ', ' '],
            ])
        for i in zip(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9]): # four possibilities are present 
            for row in i:
                if ' ' not in row:
                    print(row, end=sep)      
            print('')


    def index_2d(self, myList, v):
        for i, x in enumerate(myList):  # Find what the hell is this first
            if v in x:
                return i, x.index(v)

    def next_steps(self, mat, p=True, checkAlready =True):
                
        if mat in self.traversedState_ and checkAlready:
            return 'Already traversed'
        if p:
            print('Current Matrix:')
            self.print_matrix([mat])
        
        self.traversedState_.append(copy.deepcopy(mat))
        if p:
            print('Next Steps')
        emptyPosition = self.index_2d(mat, 0)
        result, hs, offsets = [], [], [1, -1, 0]
        orgMat = copy.deepcopy(mat)
        
        for x in offsets:
            for y in offsets:
                if abs(x + y) == 1:
                    newX = emptyPosition[0] + x
                    newY = emptyPosition[1] + y
                    if 0 <= newX <= 2 and  0 <= newY <= 2:
                    
                        mat[emptyPosition[0]][emptyPosition[1]] = mat[newX][newY]
                        mat[newX][newY] = 0
                        if mat not in self.traversedState_ and mat != [
                                [1, 2, 3],
                                [4, 5, 6],
                                [8, 7, 0]
                                ]:
                            result.append(mat)
                            self.stack.append(mat)
                            c = self.cost(copy.deepcopy(mat))
                            if p:
                                print(f'Cost: {c}', end='\t')
                            self.costStack.append(c)
                        
                        mat = copy.deepcopy(orgMat)
        if p:
            print('')
        return result


    def check_traversed(self):
        step = 0
        temp = []
        for i in range(1, len(self.traversedState_)+1):
            lastTraversed = self.traversedState_[-i:][0]
                
            if initial in self.next_steps(lastTraversed, False, False):
                self.print_matrix(temp)
                return step
            temp.append(lastTraversed)

    
    def solve(self, initial, goal):
        step = 0  
        while(initial != goal):
            step += 1
            print(f'\nStep: {step}\n')
            res = self.next_steps(initial)
            self.print_matrix(res)
            
            i = self.costStack.index((min(self.costStack)))
            temp = self.costStack.pop(i)
            if temp<self.minCost:
                self.minCost = temp
            
            print(f'Minimum cost till now: {self.minCost}')
            print(f'Stack size: {len(self.stack)}')
            
            initial = self.stack.pop(i)    
            
            
            if step > 40000:
                break
            

        print(f'\nTraversed States:')
        self.traversedState_.append(self.goal)

        for matIndex in range(0, len(self.traversedState_), 10):
            self.print_matrix(self.traversedState_[matIndex:matIndex+10])
            print("")
        
        print(f'\nSummary:\n\tSteps: {step}')

initial = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

S1 = Solver(initial, goal)