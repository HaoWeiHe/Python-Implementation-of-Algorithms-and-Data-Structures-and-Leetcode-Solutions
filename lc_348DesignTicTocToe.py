class TicTacToe(object):

    def __init__(self, n):
        """
        01 02 03
        0, 0, 0
        0, 0, 0
        0, 0, 0
        
        """
        self.n = n
        # row{1:[x,o,x],2:[x,o,o]}
       
        self.row = collections.defaultdict(list)
        self.col = collections.defaultdict(list)
        self.dia = []##0,0 1,1 2,2 /
        self.dia1 = []
         # 0,2 1,1 2,0 -> row + (n-1 -row), 
        

    def move(self, row, col, player):
        """

        :rtype: int
        """
        sgn = 1 if player%2 ==1 else -1
        self.row[row].append(sgn)
        self.col[col].append(sgn)
        
        if row == col:
            self.dia.append(sgn)
        if col == self.n - 1 -row:
            self.dia1.append(sgn)
        

        if abs(sum(self.row[row])) == self.n:
            return 1 if self.row[row][0] > 0 else 2
      
        if abs(sum(self.col[col])) == self.n:
            return 1 if self.col[col][0] > 0 else 2
        if abs(sum(self.dia)) == self.n:
            return 1 if self.dia[0] > 0 else 2
        if abs(sum(self.dia1)) == self.n:
            return 1 if self.dia1[0] >  0 else 2
        return 0
