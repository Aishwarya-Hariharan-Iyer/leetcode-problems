class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_p = 0
        # l = len(prices)
        # for i in range(l):
        #     b = prices[i]
        #     for j in range(i+1, l):
        #         s = prices[j]
        #         max_p = max(max_p, s-b)
        # return max_p

        l = len(prices)

        if l == 1:
            return 0

        max_so_far = prices[l-1]
        best_profit = 0

        for i in range(l-2, -1, -1):
            best_profit = max(best_profit, max_so_far - prices[i])
            max_so_far = max(max_so_far, prices[i])
        return best_profit
