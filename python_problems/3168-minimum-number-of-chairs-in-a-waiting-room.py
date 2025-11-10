class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return 0
            
        curr_occ = 0
        max_simul_occ = 0

        for c in s:
            if c == "E":
                curr_occ += 1
                max_simul_occ = max(curr_occ, max_simul_occ)
            if c == "L":
                curr_occ -= 1

        return max_simul_occ
        
