class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        for i in range(int(k/2)):
            row_temp = grid[x+i][y:y+k]
            grid[x+i][y:y+k] = grid[x+k-1-i][y:y+k]
            grid[x+k-1-i][y:y+k] = row_temp
        return grid
