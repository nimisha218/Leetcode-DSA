from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        def get_key(arr):
            return tuple(arr)
        
        d_row = defaultdict(int)
        for row in grid:
            d_row[get_key(row)] += 1
        
        d_col = defaultdict(int)
        for col in range(len(grid[0])):
            current_col = []
            for row in range(len(grid)):
                current_col.append(grid[row][col])
            d_col[get_key(current_col)] += 1
    
        ans = 0
        for arr in d_row:
            ans += d_row[arr] * d_col[arr]
        
        return ans
        
        