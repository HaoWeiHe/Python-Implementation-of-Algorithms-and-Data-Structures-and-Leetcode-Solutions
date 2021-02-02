"""
_ 2
1 2
"""

class TicTacToe(object):

    def __init__(self, n):
        self.row = [0]*n
        self.col = [0]*n
        self.dia = 0
        self.rev_dia = 0
        self.n = n
        # row [i] -> (-1, 1)
        # col [i] -> (-1,2)
        #dia (i,j) -> i==j
        #rev_dia = [(2,0),(1,1),(0,2)]
        # (n-1-i, i) -> (2,0) (1,1) (0,2)
        #

    def move(self, row, col, player):
        self.row[row] += 1 if player ==1 else -1
        self.col[col] += 1 if player ==1 else -1
        if row == col:
            self.dia +=1 if player ==1 else -1
        if row == self.n-1-col:
            self.rev_dia +=1 if player ==1 else -1
            
        checklist = [e for e in self.row] +  [e for e in self.col] + [self.dia] + [self.rev_dia]
        
        for e in checklist:
            if abs(e) == self.n:
                return 1 if e == self.n else 2
        return 0