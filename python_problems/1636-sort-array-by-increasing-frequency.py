class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        counts = dict({})

        for i in range(l):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
        
        arr = []
        for key in counts.keys():
            v = counts[key]
            arr = arr + [[key, v]]

        def compare(x, y):
            if x[1] < y[1]:
                return -1
            elif x[1] > y[1]:
                return 1
            elif x[0] < y[0]:
                return 1
            else:
                return -1

        arr.sort(key=cmp_to_key(compare))

        res = []

        for pair in arr:
            num = pair[0]
            times = pair[1]
            to_add = [num] * times
            res += to_add

        return res



        
