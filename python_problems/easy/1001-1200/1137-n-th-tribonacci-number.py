class Solution:

    def memoize(self, n, memo):
        if n in memo:
            return memo[n]
        memo[n] = self.memoize(n-1, memo) + self.memoize(n-2, memo) + self.memoize(n-3, memo)
        return memo[n]
    
    def tribonacci(self, n: int) -> int:
        memo = dict()
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        return self.memoize(n, memo)
        