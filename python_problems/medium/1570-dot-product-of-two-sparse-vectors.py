class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_val_pairs = dict() #e.g. 1 -> 4. Rest assumed to be 0
        self.length = len(nums)
        for i in range(self.length):
            if nums[i] != 0:
                self.index_val_pairs[i] = nums[i]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        pdt = 0
        for k in self.index_val_pairs.keys():
            pdt += self.index_val_pairs[k] * vec.index_val_pairs.get(k, 0)
        return pdt

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
