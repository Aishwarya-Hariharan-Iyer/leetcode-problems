class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: # no swap
            return True
            
        if s1[2] + s1[1] + s1[0] + s1[3] == s2: #swap 0, 2 only
            return True

        if s1[0] + s1[3] + s1[2] + s1[1] == s2: #swap 1, 3 only
            return True

        if s1[2] + s1[3] + s1[0] + s1[1] == s2: #swap both
            return True

        return False
        
            
        