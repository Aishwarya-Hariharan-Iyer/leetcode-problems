class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        missing_vals = []
        l = len(arr)
        count = 1
        last_positive_number = float('-inf')

        for i in range(l):
            if i == 0:
                diff = arr[0] - 1
                missing_vals += [j for j in range(1, diff+1)]
                last_positive_number = max(last_positive_number, arr[0])
            else:
                diff = arr[i] - arr[i-1]
                missing_vals += [j for j in range(last_positive_number+1, last_positive_number+diff)]
                last_positive_number = max(last_positive_number, arr[i])

        print(missing_vals)
        if k-1 <len(missing_vals):
            return missing_vals[k-1]
        else:
            return last_positive_number + (k - len(missing_vals))

        
