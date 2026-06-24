class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        count = 0

        i = 0
        j = n-1

        while i < m and j >= 0:
            curr = grid[i][j]
            if curr < 0:
                count += m - i
                j -= 1 # move LEFT in same row
            else:
                i += 1 # move DOWN in same col
        
        return count


        
        
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        As soon as we find a neg. no. at r, c, as it's non-increasing, every num[r', c'] if r' > r or c' > c is neg.
        '''
        count = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0:
                    #all grid[i][j] AFTER it is negative.
                    #since the 'j'....cols is negative, every grid[i'][j'] wherej' > j is also negative for any i
                    count += cols - j
                    break
        
        return count

        