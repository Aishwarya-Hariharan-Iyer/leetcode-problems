class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        l = len(items)

        if l == 0:
            return []

        student_scores = dict({})

        for i in range(l):
            stu_id = items[i][0]
            score = items[i][1]
            student_scores[stu_id] = student_scores.get(stu_id, []) + [score]
        
        ans = []

        for key in student_scores.keys():
            scores = student_scores[key]
            scores.sort(key=lambda x: -x)
            scores = scores[:5]
            avg_sum = sum(scores)/5
            ans += [[key, avg_sum]]
        
        ans.sort(key=lambda x: x[0])
        return ans
