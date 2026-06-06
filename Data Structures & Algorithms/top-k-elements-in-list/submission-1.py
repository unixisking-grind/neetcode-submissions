class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        obj = {}
        
        for i, num in enumerate(nums):
            obj[num] = 0

        for i, num in enumerate(nums):
            obj[num] += 1

        maxOccurrences = sorted(obj, key = lambda x: obj[x], reverse=True)

        return maxOccurrences[:k]



            



        