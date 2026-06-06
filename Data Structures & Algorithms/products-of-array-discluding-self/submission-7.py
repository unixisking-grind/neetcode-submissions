from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        acc = 1
        for num in nums:
            result.append(acc)
            acc *= num

        acc = 1
        i = len(nums) - 1
        while i >= 0:
            result[i] = result[i] * acc
            acc *= nums[i]
            i -= 1

        return result