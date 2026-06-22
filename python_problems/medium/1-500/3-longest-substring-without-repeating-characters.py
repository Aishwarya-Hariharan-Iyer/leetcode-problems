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
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l
        lp = 0
        rp = 0
        best_len = 0
        curr_len = 0
        recent_chars = dict()
        while rp < l:
            if recent_chars.get(s[rp], -1) == -1: #unique so advance
                curr_len += 1
            else:
                last_pos = recent_chars.get(s[rp])
                if last_pos >= lp:
                    lp = last_pos + 1
                curr_len = rp - lp + 1
            best_len = max(best_len, curr_len)
            recent_chars[s[rp]] = rp
            rp += 1

        return best_len


