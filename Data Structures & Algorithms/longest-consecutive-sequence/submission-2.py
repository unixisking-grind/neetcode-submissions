class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashset = set()

        for num in nums:
            hashset.add(num)
        
        sortedList = sorted(list(hashset))

        longestSequences = []

        print(sortedList)
        count = 1
        for i in range(1, len(sortedList)):
            if i > 0:
                # Ongoing sequence
                if sortedList[i] - sortedList[i-1] == 1:
                    count += 1
                # No sequence we simply keep moving
                elif count == 1:
                    continue
                # count > 0 and sequence is done: add length and reset
                else:
                    longestSequences.append(count)
                    count = 1
        
        if count > 1:
            longestSequences.append(count)

        if len(sortedList) > 0 and len(longestSequences) == 0:
            return 1
            
        print(longestSequences)

        return max(longestSequences)


            



        