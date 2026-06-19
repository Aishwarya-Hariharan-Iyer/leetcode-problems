import math

class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                val2 = i**2 + j**2
                val = math.sqrt(val2)
                if val - int(val) == 0 and val <= n:
                    count += 1
                elif val > n:
                    break
        return count
