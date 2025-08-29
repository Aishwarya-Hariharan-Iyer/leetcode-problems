class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []

        l = len(nums)

        if l == 0:
            return []

        if l == 1:
            return [str(nums[0])]

        curr_range = []

        for i in range(l):
            if len(curr_range) == 0:
                curr_range.append(nums[i])
            elif len(curr_range) == 1:
                if nums[i] - curr_range[0] == 1:
                    curr_range.append(nums[i])
                else:
                    ranges += [str(curr_range[0])]
                    curr_range[0] = nums[i]
            else:
                if nums[i] - curr_range[1] == 1:
                    curr_range[1] = nums[i]
                else:
                    str_to_add = str(curr_range[0]) + "->" + str(curr_range[1])
                    ranges += [str_to_add]
                    curr_range = [nums[i]]
        
        
        if len(curr_range) == 1:
            ranges += [str(curr_range[0])]
        else:
            str_to_add = str(curr_range[0]) + "->" + str(curr_range[1])
            ranges += [str_to_add]
        return ranges
        
