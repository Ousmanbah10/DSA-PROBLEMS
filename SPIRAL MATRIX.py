
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

  
        rows = len(matrix)
        cols = len(matrix[0])
        current = []
        if matrix == [[1]]:
            return [1]
        going_right, going_down, going_left, going_up = 0, cols - 1, rows - 1, 0
        n = rows * cols

        while len(current) < n:
            # go right (exclude last col, next loop handles it)
            for i in range(going_right, going_down):
                current.append(matrix[going_up][i])
            if len(current) == n: break

            # go down (exclude last row, next loop handles it)
            for i in range(going_up, going_left):
                current.append(matrix[i][going_down])
            if len(current) == n: break

            # go left (exclude first col, next loop handles it)
            for i in range(going_down, going_right, -1):
                current.append(matrix[going_left][i])
            if len(current) == n: break

            # go up (exclude first row, next loop handles it)
            for i in range(going_left, going_up, -1):
                current.append(matrix[i][going_right])
            if len(current) == n: break

            # shrink boundaries
            going_right += 1
            going_down -= 1
            going_left -= 1
            going_up += 1

            
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

  
        rows = len(matrix)
        cols = len(matrix[0])
        current = []
        if matrix == [[1]]:
            return [1]
        going_right, going_down, going_left, going_up = 0, cols - 1, rows - 1, 0
        n = rows * cols

        while len(current) < n:
            # go right (exclude last col, next loop handles it)
            for i in range(going_right, going_down):
                current.append(matrix[going_up][i])
            if len(current) == n: break

            # go down (exclude last row, next loop handles it)
            for i in range(going_up, going_left):
                current.append(matrix[i][going_down])
            if len(current) == n: break

            # go left (exclude first col, next loop handles it)
            for i in range(going_down, going_right, -1):
                current.append(matrix[going_left][i])
            if len(current) == n: break

            # go up (exclude first row, next loop handles it)
            for i in range(going_left, going_up, -1):
                current.append(matrix[i][going_right])
            if len(current) == n: break

            # shrink boundaries
            going_right += 1
            going_down -= 1
            going_left -= 1
            going_up += 1

            if len(current) == n-1:
                current.append(matrix[going_right][going_up])
                return current
        return current
        return current