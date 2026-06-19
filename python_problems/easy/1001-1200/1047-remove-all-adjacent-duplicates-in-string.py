class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = ""
        for c in s:
            if answer == "" or answer[-1] != c:
                answer += c
            else:
                answer = answer[:-1]

        return answer
        
