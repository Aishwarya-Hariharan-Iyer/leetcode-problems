class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit_s = '{:032b}'.format(n)
        bit_s = map(lambda x: int(x), bit_s)
        return sum(bit_s)       
