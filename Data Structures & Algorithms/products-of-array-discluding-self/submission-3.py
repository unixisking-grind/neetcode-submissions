class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        result = []
        hasZero = 0
        for n in nums:
            if n != 0:
                acc *= n
            else:
                hasZero += 1
            
        for i, n in enumerate(nums):
            if hasZero > 1:
                result.append(0)
            elif n == 0 and hasZero > 0:
                result.append(acc)
            elif n != 0 and hasZero > 0:
                result.append(0)
            else:
                result.append(int(acc / n))

        return result

        