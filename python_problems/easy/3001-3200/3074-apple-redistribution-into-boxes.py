class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total_apples = sum(apple)
        curr_cap = 0
        num = 0
        capacity.sort(reverse=True)
        for c in capacity:
            curr_cap += c
            num += 1
            if curr_cap >= total_apples:
                return num
        return num
        
