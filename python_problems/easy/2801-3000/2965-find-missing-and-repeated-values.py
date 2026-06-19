class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = -1
        n = len(grid)
        track = dict()
        expected_sum = (n**2)*(n**2 + 1)/2

        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                if track.get(num, 0) == 0:
                    track[num] = 1
                    expected_sum -= num
                else:
                    a = num # found repeated number
        
        return [a, int(expected_sum)]

                    