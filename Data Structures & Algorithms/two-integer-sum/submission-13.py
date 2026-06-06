class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        {diff: index}
        """
        obj = {}

        for i, num in enumerate(nums):
            diff = target - num
            if num in obj:
                return [obj[num], i]
            obj[diff] = i
        
        return []
        
        