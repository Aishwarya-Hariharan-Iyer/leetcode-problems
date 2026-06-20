class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        tl = 0

        cost.sort()
        l = len(cost)
        
        #for max costly free candies we make 'triples' from right end
        tl = tl + sum(cost) 

        #account for free candies
        for i in range(l-3, -1, -3):
            tl -= cost[i]

        return tl 

        