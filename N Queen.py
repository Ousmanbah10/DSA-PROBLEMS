class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        if n == 1:
            return [["Q"]]

        def is_Valid(r,c,nums):
            
            
            for element1, element2 in nums:
                if c == element2:
                    return False    
                if r == element1:
                    return False

                if abs(element1 - r) == abs(element2 - c):
                    return False
            return True
        
        output = []
        def place(current,row):

            if row == n:
                if row == n:
                    board = [["."] * n for _ in range(n)]
                    for i, j in current:
                        board[i][j] = "Q"
                    output.append(["".join(row) for row in board]) 
                    return
            for c in range(n):

                if is_Valid(row,c,current):
                    current.append((row,c))
                    place(current,row+1)
                    current.pop()

        place([],0)
        return output