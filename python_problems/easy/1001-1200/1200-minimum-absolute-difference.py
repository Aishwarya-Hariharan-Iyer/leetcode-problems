class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        min_diff = float('inf')
        l = len(arr)

        for i in range(1, l):
            min_diff = min(abs(arr[i] - arr[i-1]), min_diff)

        pairs = []
        for i in range(1, l):
            d = abs(arr[i] - arr[i-1])
            if d == min_diff:
                pairs.append([arr[i-1], arr[i]])

        return pairs




        
