class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        l = len(intervals)
        if l <= 1:
            return True
        intervals.sort()
        for i in range(1, l):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
        