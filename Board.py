import pandas as pd
from copy import deepcopy

doubleSpaces = [4,6,8]
doubleIndices = [11,12,13]

class Board():
    # creates a standard board
    # first position is not usable
    board = None
    prevNumMoved = None
    totalMoves = 0

    def __init__(self):
        self.board = [0 for i in range(14)]
        for i in range(2,10): self.board[i] = i
        self.board[0] = -1
        self.board[10] = 1
    
    def copy(self):
        c = Board()
        c.board = deepcopy(self.board)
        c.prevNumMoved = self.prevNumMoved
        c.totalMoves = self.totalMoves
        return c

    def display(self):
        a = pd.Series(self.board[1:11])
        b = pd.Series([' ',' ',' ', self.board[11], ' ', self.board[12], ' ', self.board[13], ' ', ' '])
        df = pd.DataFrame([b,a])
        return df.to_string(index=False, header=False)

# FOR CHECKDOWN AND CHECKUP:
# i : NUMBER whose above/below positions will be checked. Will return a tuple: (is valid move, index of checked space)
# i must be in one of the 3 spaces below one of the 'trench recesses'
    def checkDown(self, i):
        try:
            x = self.board.index(i)
            if self.board.index(i) in doubleIndices:
                if self.board[ doubleSpaces[ doubleIndices.index(x) ] ] == 0: 
                    return (True, doubleSpaces[ doubleIndices.index(x) ] )
        except:
            return (False, None)

        return (False, None)

    def checkUp(self, i):
        try:
            x = self.board.index(i)
            if self.board.index(i) in doubleSpaces:
                if self.board[ doubleIndices[ doubleSpaces.index(x) ] ] == 0: 
                    return (True, doubleIndices[ doubleSpaces.index(x) ] )
        except:
            return (False, None)

        return (False, None)

# FOR CHECKLEFT AND CHECKRIGHT:
# i : NUMBER whose left/right position will be checked. Will return a tuple: (is valid a move, index of checked space)
# if i is in doubleIndices, it will automatically return (False, None)

    def checkLeft(self, i):
        try:
            x = self.board.index(i)
            if x not in doubleIndices:
                if self.board[x-1] == 0: return (True, x-1)
        except:
            return (False, None)

        return (False, None)

    def checkRight(self, i):
        try:
            x = self.board.index(i)
            if x not in doubleIndices:
                if self.board[x+1] == 0: return (True, x+1)
        except:
            return (False, None)
        return (False, None)


# i : number whose possible moves will be returned
# finalset keeps track of all SEEN valid moves from current position
# currentset keeps track of unexplored states

    def possibleMoves(self, i):
        finalset = [self.board.index(i)]
        currentset = []

        up = self.checkUp(i)
        down = self.checkDown(i) 
        left = self.checkLeft(i) 
        right = self.checkRight(i)  

        if up[0]: finalset.append(up[1]); currentset.append(up[1])
        if down[0]: finalset.append(down[1]); currentset.append(down[1])
        if left[0]: finalset.append(left[1]); currentset.append(left[1])
        if right[0]: finalset.append(right[1]); currentset.append(right[1])
        
        while currentset:
            temp = self.copy()
            temp.move( (i, currentset[len(currentset) - 1]) )
            currentset = currentset[:-1]

            up = temp.checkUp(i)
            down = temp.checkDown(i)
            left = temp.checkLeft(i)
            right = temp.checkRight(i)    

            if up[0]:
                if not (up[1] in finalset): 
                    finalset.append(up[1])
                    currentset.append(up[1])
            if down[0]:
                if not (down[1] in finalset): 
                    finalset.append(down[1])
                    currentset.append(down[1])
            if left[0]:
                if not (left[1] in finalset): 
                    finalset.append(left[1])
                    currentset.append(left[1])
            if right[0]:
                if not (right[1] in finalset): 
                    finalset.append(right[1])
                    currentset.append(right[1])

        return finalset
        

    # executes a valid move
    # move - tuple (number, new position)
    def move(self, move):
        self.board[self.board.index(move[0])] = 0
        self.board[move[1]] = move[0]
        if self.prevNumMoved == move[0]:
            return
        else:
            self.prevNumMoved = move[0]
            self.totalMoves += 1

