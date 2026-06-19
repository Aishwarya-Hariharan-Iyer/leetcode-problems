class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_arr = []
        count_dict = dict()
        for elem in nums:
            if not (elem in temp_arr):
                temp_arr += [elem]
                count_dict.update({elem: 1})
            else:
                curr = count_dict.get(elem)
                if curr == 1:
                    temp_arr += [elem]
                    count_dict.update({elem: 2})
        
        count = len(temp_arr)
        for i in range(count):
            nums[i] = temp_arr[i] 

        return count