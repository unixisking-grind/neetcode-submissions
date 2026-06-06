from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = []

        acc = 1
        for num in nums:
            prefixArr.append(acc)
            acc *= num

        suffixArr = deque()
        acc = 1
        for num in reversed(nums):
            suffixArr.appendleft(acc)
            acc *= num

        i = 0
        result = []
        for num in suffixArr:
            result.append(num * prefixArr[i])
            i += 1

        return result

        