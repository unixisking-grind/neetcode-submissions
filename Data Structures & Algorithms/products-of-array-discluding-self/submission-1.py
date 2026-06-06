from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = reduce(lambda acc,x: x*acc if x != 0 else acc, nums)
        res = []

        print(product)
        for i, num in enumerate(nums):
            if 0 in nums[:i] + nums[i+1:]:
                res.append(0)
            elif num == 0:
                res.append(product)
            else:
                res.append(int(product/num))
        return res

        
        