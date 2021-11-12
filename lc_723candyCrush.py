class Solution(object):
    def candyCrush(self, board):
        """
        while :
            1) labeled 
            2) emilate
            until no one be labeled
        
        1) labeled:  / update function
        go col_1
            row[1]: [5,211,311,411,1,4,,1,1,1,1]
                    [1,1,    1, 1  1  1 1 2 3 4]
                    [5,211,311,411,1,4,,1,1,1,1]
                    update(row_idx, >3idx, >3val)
            happend = True
            row[0]
        go row:
            col1 [1,1,2,2,2]
            row_8, idex 2,3,4 change to -1
        
        2)  
         [5,211,-1,411,1,4, -1, -1, -1, -1]
          c = count (-1)
          [-1,-1,-1,-1,5,211,411,1,4]
          all back to c space, except -1
         changecol()
         
         3) until happend = False
        """
        
        num_cols, num_rows = len(board), len(board[0])
        
        def crash():
            #labeled

            flag = False
            cols, rows = [[1] * num_rows for _ in range(num_cols)], [[1]* num_cols for _ in range(num_rows)]
            
            for i in range(num_cols):
                for j in range(1,num_rows):
                    if board[i][j] == 0:
                        continue
                    if board[i][j] == board[i][j - 1]:
                        cols[i][j] += cols[i][j-1]
            
            for j in range(num_rows):
                for i in range(1, num_cols):
                    if board[i][j] == 0:
                        continue
                    if board[i][j] == board[i - 1][j]:
                        rows[j][i] += rows[j][i-1]
  
            for r_idx, lst in enumerate(rows):
                for c_idx, c_val in enumerate(lst):
                    if c_val >= 3:
                        flag = True
                        for i in range(c_val):
                            board[c_idx - i][r_idx] = -1

            for c_idx, lst in enumerate(cols):
                for r_idx, r_val in enumerate(lst):
                    if r_val >= 3:
                        flag = True
                        for i in range(r_val):
                            board[c_idx][r_idx - i] = -1
            #emute
            # print("=====")
            # for ele in board:
            #     s = ""
            #     for e in ele:
            #         s += "%5s"%(e)
            #     print(s)
            for row_idx in range(num_rows):
                counter = 0 
                new_lst  = []

                for col_idx in range(num_cols):
                    ele = board[col_idx][row_idx]
                    if ele != -1:
                        new_lst.append(ele)
                    else:
                        counter += 1
                new_lst = [0] * counter + new_lst

                for idx in range(num_cols):
                    board[idx][row_idx] = new_lst[idx]

        
            return flag
        while True:
            if crash():
                continue
            break
        return board
                