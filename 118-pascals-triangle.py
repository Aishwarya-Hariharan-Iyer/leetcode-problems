class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        if numRows == 0:
            return res

        def get_next_pascal_row(arr):
            l = len(arr)
            ans = [0] * (l+1)
            ans[0] = 1
            ans[-1] = 1
            for i in range(1, l):
                ans[i] = arr[i-1] + arr[i]
            return ans
        
        for i in range(1, numRows+1):
            row = []
            if i == 1:
                row = [1]
                res += [row]
            elif i == 2:
                row = [1, 1]
                res += [row]
            else:
                row = get_next_pascal_row(res[-1])
                res += [row]

        return res
