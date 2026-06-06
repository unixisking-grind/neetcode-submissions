class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashset = set()
        for num in nums:
            hashset.add(num)

        maxCount = 0
        for num in hashset:
            prev = num - 1
            if prev not in hashset:
                count = 1
                for i in range(1, len(hashset)):
                    currentNum = num + i
                    if currentNum in hashset:
                        count += 1
                    else:
                        break
                
                if count > maxCount:
                    maxCount = count
                count = 1

        return maxCount