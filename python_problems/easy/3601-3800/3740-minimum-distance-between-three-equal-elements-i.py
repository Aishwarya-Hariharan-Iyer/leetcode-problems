from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        l = len(nums)
        if l < 3:
            return -1

        pos = defaultdict(list)

        for i in range(l):
            pos[nums[i]].append(i)
        
        found_good_tuple = False
        min_dist = float('inf')

        for k in pos.keys():
            indices = pos[k]
            if len(indices) < 3:
                continue
            found_good_tuple = True
            li = len(indices)
            dist = float('inf')
            for i in range(li):
                i1 = indices[i]
                for j in range(i+1, li):
                    i2 = indices[j]
                    for k in range(j+1, li):
                        i3 = indices[k]
                        d = abs(i1-i2) + abs(i2-i3) + abs(i1-i3)
                        dist = min(dist, d)
            min_dist = min(min_dist, dist) 
        
        return -1 if not found_good_tuple else min_dist

        

        