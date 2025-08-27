class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]

        def get_next_row(arr):
            n = len(arr) + 1
            ans = [1] + [0] * (n-2) + [1]
            for i in range(1, n-1):
                ans[i] = arr[i-1] + arr[i]
            return ans
        res = [[1], [1, 1]]
        
        for i in range(2, rowIndex+1):
            res += [get_next_row(res[i-1])]
        
        return res[-1]
        
        
