class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        n_str = str(n)
        l = len(n_str)

        squares = dict({})
        
        while True:
            sum_of_squares = sum(map(lambda x: int(x) ** 2, n_str))
            if sum_of_squares == 1:
                return True
            if squares.get(sum_of_squares, -1) != -1:
                return False
            squares[sum_of_squares] = 1
            n_str = str(sum_of_squares)

        
