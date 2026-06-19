class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        l = len(strs[0])
        count = 0

        for i in range(l):
            col = list(map(lambda x: x[i], strs))
            for k in range(1, n):
                if col[k] < col[k-1]:
                    count += 1
                    break
        
        return count

        
