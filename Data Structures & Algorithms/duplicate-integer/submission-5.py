"""
Find dups: return true if that's the case
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        numsSet = set()
        for num in nums:
            if num in numsSet:
                return True
            else:
                numsSet.add(num)
        return False
        

         