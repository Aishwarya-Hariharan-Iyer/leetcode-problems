class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = [0] * (n+1)

        for i in range(n+1):
            num = str(bin(i))[2:]
            num = map(lambda x: int(x), num)
            arr[i] = sum(num)

        return arr
