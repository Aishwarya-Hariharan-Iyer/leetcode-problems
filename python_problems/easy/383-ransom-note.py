class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lr = len(ransomNote)
        lm = len(magazine)

        if lm < lr:
            return False

        mag = dict({})
        ran = dict({})
        
        for m in magazine:
            mag[m] = mag.get(m, 0) + 1
        
        for r in ransomNote:
            ran[r] = ran.get(r, 0) + 1
        
        for r in ran.keys():
            if ran[r] > mag.get(r, 0):
                return False
        
        return True


        
