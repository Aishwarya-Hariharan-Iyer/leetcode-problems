class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n == 1:
            return 1

        i = 1
        coins = n 

        while coins > 0:
            if i > coins: #incomplete or impossible row
                break
            coins -= i
            i += 1
        return i-1


        