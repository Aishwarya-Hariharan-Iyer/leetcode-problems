class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        d1 = dict()
        for num in nums1:
            d1[num] = 1
        for num in nums2:
            if d1.get(num, 0) != 0:
                return num
        return -1 #error

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        if nums1 == [] or nums2 == []:
            return []

        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]

            # advance smaller value ptr
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return -1 #error
