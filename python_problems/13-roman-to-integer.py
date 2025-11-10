class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = dict({"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900})

        l = len(s)
        i = 0
        ans = 0

        while i < l:
            c = s[i]
            if i < l-1 and c == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                c = s[i] + s[i+1]
                i += 1
            elif i < l-1 and c == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                c = s[i] + s[i+1]
                i += 1
            elif i < l-1 and c == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                c = s[i] + s[i+1]
                i += 1
            ans += vals[c]
            i += 1

        return ans
