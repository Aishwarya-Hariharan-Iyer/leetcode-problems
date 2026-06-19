class Solution:
    def reverseVowels(self, s: str) -> str:

        l = len(s)
        lp = 0
        rp = l-1

        vowels = dict({"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "A": 1, "E": 1, "I": 1, "O": 1, "U": 1})
        s = list(s)

        while rp > lp:
            if vowels.get(s[lp], 0) == 1 and vowels.get(s[rp], 0) == 1:
                temp = s[lp]
                s[lp] = s[rp]
                s[rp] = temp
                lp += 1
                rp -= 1
            elif vowels.get(s[lp], 0) == 1:
                rp -= 1
            elif vowels.get(s[rp], 0) == 1:
                lp += 1
            else:
                rp -= 1
                lp += 1

        return "".join(s)
            
        
