class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        def shift_by_one(word, l):
            if l == 0 or l == 1:
                return word
            
            return word[-1] + word[:l-1]
        
        word = s
        l = len(word)
        g = len(goal)

        if l != g:
            return False

        if word == goal:
            return True

        while True:
            word = shift_by_one(word, l)
            if word == goal:
                return True
            if word == s:
                break 
        
        return False

                
