class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeated = dict()
        for n in nums:
            if repeated.get(n, -1) != -1:
                return n
            repeated[n] = 1

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        repeats = dict()
        
        for n in nums:
            repeats[n] = repeats.get(n, 0) + 1

        for k in repeats.keys():
            if repeats[k] != 1:
                return k

        return -1
