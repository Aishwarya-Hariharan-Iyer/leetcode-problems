class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l % 2 == 1:
            return False

        bracket_dict = dict({'{': '}', '[':']', '(': ')'})
        
        open_brackets = []
        count_op = 0
        count_cl = 0
        
        for b in s:
            if b == "{" or b == "[" or b == "(":
                open_brackets.append(b)
                count_op += 1
                if count_op > l/2:
                    return False
            else:
                if len(open_brackets) == 0:
                    return False
                pair_a = open_brackets.pop()
                if b != bracket_dict[pair_a]:
                    return False
                count_cl += 1
                if count_cl > l/2:
                    return False
        return True
                
