class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashset = set()

        for num in nums:
            hashset.add(num)


        sequence = set()
        starts = []
        for num in hashset:
            prev = num - 1
            if prev not in hashset:
                ## do work
                starts.append(num)

        lenght = len(hashset)
        count = 1
        counts = []
        for start in starts:
            for i in range(1, len(hashset)):
                currentNum = start + i
                if currentNum in hashset:
                    count += 1
                else:
                    break
            
            counts.append(count)
            count = 1


        print(starts)
        print(sorted(list(hashset)))
        print(counts)
        return max(counts)


        


            



        