class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        sent = set(sentence)
        l = len(sent)
        if l < 25:
            return False
        for i in range(97, 123):
            if chr(i) not in sent:
                return False
        return True
