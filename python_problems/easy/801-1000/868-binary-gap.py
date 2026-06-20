class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        prev_pos = -1
        n = str(bin(n))
        for i in range(len(n)):
            if n[i] == "1" and prev_pos == -1:
                prev_pos = i #first 1
            elif n[i] == "1": #already has prev pos
                dist = i - prev_pos
                max_dist = max(max_dist, dist)
                prev_pos = i
            #else do nothing
        return max_dist
        