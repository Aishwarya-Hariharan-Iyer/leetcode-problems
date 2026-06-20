from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = len(str1)
        s2 = len(str2)

        if str1 + str2 != str2 + str1:
            return ""

        g = gcd(s1, s2)
        return str1[:g]
        

        