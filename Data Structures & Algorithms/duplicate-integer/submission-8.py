class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
            
        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        
        return False
        