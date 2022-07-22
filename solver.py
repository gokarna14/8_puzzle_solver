from cmath import inf
import copy


initial = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
traversedState_ = []

stack = []
minH = 1000


def print_matrix(mat, sep = ' '):
    a = [i for i in mat]
    
    while(len(a)<3):
        a.append([
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ])
    for i, j, k in zip(a[0], a[1], a[2]): # four possibilities are present 
        print(i, end = sep)
        if ' ' not in j:
            print(j, end=sep)
        if ' ' not in k:
            print(k, end=sep)
        print('')


def index_2d(myList, v):
    for i, x in enumerate(myList):  # Find what the hell is this first
        if v in x:
            return i, x.index(v)

def cost(goalMat, toCompareMat, traversedState = []):
    if toCompareMat in traversedState:
        return inf
    try:
        result = 0
        if not len(goalMat) == len(toCompareMat):
            print('Size of matrix to compare should be same !!')
            return
        for rowIndex in range(len(goalMat)):
            for columnIndex in range(len(goalMat[rowIndex])):
                if goalMat[rowIndex][columnIndex] != toCompareMat[rowIndex][columnIndex]:
                    (goalRowIndex, goalColumnIndex) = index_2d(goalMat, toCompareMat[rowIndex][columnIndex])
                    rowChange = abs(goalRowIndex - rowIndex)
                    columnChange = abs(goalColumnIndex - columnIndex)
                    result += rowChange + columnChange
        return result

    except TypeError:
        print('Please enter the 2D matrix of the same size!!\n')

def next_steps(mat):
    
    if mat not in traversedState_:
        traversedState_.append(copy.deepcopy(mat))
    print('\nCurrent State:')
    print_matrix([mat])
    print(f'Next Steps: ')
    
    result, hs, offsets = [], [], [1, -1, 0]
    orgMat = copy.deepcopy(mat)
    
    emptyPosition = index_2d(mat, 0)
    for x in offsets:
        for y in offsets:
            if abs(x + y) == 1:
                
                newX = emptyPosition[0] + x
                newY = emptyPosition[1] + y
                if 0 <= newX <= 2 and  0 <= newY <= 2:
                
                    mat[emptyPosition[0]][emptyPosition[1]] = mat[newX][newY]
                    mat[newX][newY] = 0
                    result.append(mat)
                    
                    # stack.append(mat)
                    
                    H = cost(goal, mat, traversedState_)
                    
                    print(f'h: {H}', end='\t')
                    hs.append(H)
                    
                    mat = copy.deepcopy(orgMat)
    print('')
    
    minHs = min(hs)
    for matrix, h in zip(result, hs):
        if h != minHs:
            stack.append(matrix)
    
    global minH
    if minH > minHs:
        minH = minHs
        
    return result, result[hs.index(minHs)]


print('\nInitial State\tGoal State')
print_matrix([initial, goal], '\t')


step = 0
while(initial != goal):
    # print(traversedState_)
    step += 1
    print(f'\nStep: {step}\n')
    res = next_steps(initial)
    print_matrix(res[0])
    initial = res[1]
    
    
    print('\nBest Next State:\n------------')
    print_matrix([initial])
    print(f"------------\nMin h till now: {minH}")
    
    
    # for mat in traversedState_:
    #     print_matrix([mat])

    print("\nTraversed Matrix:\n")

    print_matrix(traversedState_.append(goal))
