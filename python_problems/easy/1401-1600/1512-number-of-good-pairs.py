class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        l = len(nums)
        rp = l-1
        track = dict() #(num -> most recent index, most recent count)
        
        while rp >= 0:
            curr = nums[rp]
            i, c = track.get(curr, (-1, -1))
            if i == -1 and c == -1:
                track[curr] = (rp, 1)
                rp -= 1
            else:
                count += c # we can pair with each rightside element
                track[curr] = (rp, c+1)
                rp -= 1
        
        return count


        