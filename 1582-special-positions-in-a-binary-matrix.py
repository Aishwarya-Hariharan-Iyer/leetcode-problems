class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        count = 0
        m = len(mat)
        n = len(mat[0])

        acceptable_rows = []
        acceptable_cols = []

        for i in range(m):
            if sum(mat[i]) == 1:
                acceptable_rows += [i]

        for j in range(n):
            col = [row[j] for row in mat]
            if sum(col) == 1:
                acceptable_cols += [j]
        

        for i in acceptable_rows:
            for j in acceptable_cols:
                if mat[i][j] == 1:
                    count += 1
        
        return count

        
