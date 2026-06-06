class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        hashSet = set()
        for num in nums:
            hashSet.add(num)

        count = 0
        counts = []
        for num in hashSet:
            if num - 1 not in hashSet:
                i = num
                while i in hashSet:
                    count+=1
                    i+=1
                if count > 0:
                    counts.append(count)
                    count = 0

        return max(counts) if len(counts) > 0 else 0