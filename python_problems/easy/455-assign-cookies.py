class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        lg = len(g)
        ls = len(s)

        gp = 0
        sp = 0
        num = 0

        while sp < ls and gp < lg:
            if g[gp] <= s[sp]: #match found
                num += 1
                gp += 1
                sp += 1
            else: #inc cookie size
                sp += 1


        return num
