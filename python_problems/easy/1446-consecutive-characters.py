class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_power = 1
        curr_power = 1
        curr_char = ''
        for c in s:
            if curr_char == '':
                curr_char = c
            elif curr_char == c:
                curr_power += 1
            else:
                max_power = max(max_power, curr_power) 
                curr_power = 1
                curr_char = c

        max_power = max(max_power, curr_power) 
        return max_power
            
        
