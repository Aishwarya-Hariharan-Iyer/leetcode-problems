class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        best_count = [0]*l
        for i in range(l):
            tracker = dict({})
            tracker[s[i]] = 1
            best_count[i] = best_count[i] + 1
            for j in range(i+1, l):
                if tracker.get(s[j], 0) > 0:
                    break
                else:
                    tracker[s[j]] = 1
                    best_count[i] = best_count[i] + 1
        return max(best_count)

