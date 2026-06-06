class Solution:
    """
    Return the indicies i and j such as:
        nums[i] + nums[j] == target
    returns [i, j] with i != j

    thinking:
        loop through the array:
            add the number:index to a dict
            check if diff = target - num is in dict
            if so return both the currentIndex, dict[diff] 
            else add number:index and keep going

            return the answer with the smallest index first
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numsDict:
                return sorted([i, numsDict[diff]])
            else:
                numsDict[num] = i
        
        