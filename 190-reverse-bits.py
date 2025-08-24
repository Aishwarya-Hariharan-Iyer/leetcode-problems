class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_s = '{:032b}'.format(n)
        l = len(bin_s)
        arr = [0]*l
        for i in range(l):
            j = l-1-i
            arr[j] = bin_s[i]
        bin_o = "".join(arr)
        return int(bin_o, 2)
