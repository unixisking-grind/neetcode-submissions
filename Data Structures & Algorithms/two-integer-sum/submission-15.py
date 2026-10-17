class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        target - num[i] = the value I'm looking for
        Need the index of the value
        Steps:
        Store the indexs in a map {value: index}
        loop and calc target - num[i] and check in map
        if True:
            return [i, map[target]] compare them before returning
        """
        indexes = {}
        for i in range(len(nums)):
            num = nums[i]
            indexes[num] = i
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in indexes and indexes[val] != i:
                secondIndex = indexes[val]
                if i > secondIndex:
                    return [secondIndex, i]
                else:
                    return [i, secondIndex]
            
        
        