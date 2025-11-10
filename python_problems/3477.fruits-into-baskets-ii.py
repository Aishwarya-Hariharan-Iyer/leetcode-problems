class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """

        count = 0
        l = len(baskets)

        for fruit_count in fruits:
            isPlaced = False
            for i in range(l):
                if baskets[i] >= fruit_count:
                    baskets[i] = 0
                    isPlaced = True
                    break
            if not isPlaced:
                count += 1
        
        return count
            



        
