class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        ans = [-1] * l1

        if l1 == 0 or l2 == 0:
            return []

        for j in range(l1):
            num = nums1[j]
            isFound = False
            for i in range(l2):
                if nums2[i] == num:
                    isFound = True
                if isFound and nums2[i] > num:
                    ans[j] = nums2[i]
                    break
        
        return ans

                    


        
