from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        ROWS, COLS = len(matrix), len(matrix[0])
        # Padded matrix of size (ROWS + 1) x (COLS + 1)
        self.sumMat = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMat[r][c + 1]
                self.sumMat[r + 1][c + 1] = prefix + above
         

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        # Shift all coordinates by +1 to account for our 1-indexed padded prefix matrix
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
         
        bottomRight = self.sumMat[r2][c2]
        above       = self.sumMat[r1 - 1][c2]
        left        = self.sumMat[r2][c1 - 1]  # Fixed: Changed c2 to c1 - 1
        topLeft     = self.sumMat[r1 - 1][c1 - 1]
        
        # Inclusion-Exclusion Principle
        return bottomRight - above - left + topLeft