class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_mat = [1] * (n+1)
        if n == 0 or n == 1:
            return 1
        for i in range (2, n+1):
            count_mat[i] = count_mat[i-1] + count_mat[i-2]
        return count_mat[n]
