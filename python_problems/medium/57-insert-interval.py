class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        l = len(intervals)

        if l == 0:
            return [newInterval]

        new_arr = []

        for i in range(l):
            num = intervals[i]
            if num[0] > newInterval[0]:
                new_arr = intervals[:i]
                new_arr.append(newInterval)
                new_arr = new_arr + intervals[i:]
                break
        
        if len(new_arr) == 0:
            new_arr = intervals + [newInterval]
        elif len(new_arr) == l:
            new_arr = new_arr + [newInterval]

        
        merged_arr = []
        latest_pair = new_arr[0]

        for i in range(l+1):
            num = new_arr[i]
            if num[0] <= latest_pair[1]:
                latest_pair[1] = max(num[1], latest_pair[1])
                latest_pair[0] = min(num[0], latest_pair[0])
            else:
                merged_arr = merged_arr + [latest_pair]
                latest_pair = num
        
        merged_arr = merged_arr + [latest_pair]

        return merged_arr

