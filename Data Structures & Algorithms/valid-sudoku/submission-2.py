import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use a tuple (r // 3, c // 3) as the key for squares
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[r][c] == ".":
                    continue
                
                # Fixed: Use consistent tuple keys for the squares dictionary
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c]) # Fixed: Changed rows[c] to rows[r]
                squares[(r // 3, c // 3)].add(board[r][c]) # Fixed: Corrected spelling to squares
                
        return True # Fixed: Outdent so it runs only after checking the entire board