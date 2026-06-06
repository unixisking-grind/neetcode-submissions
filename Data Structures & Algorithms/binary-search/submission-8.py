class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)

        while(nums[mid] != target and left <= right):
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

            mid = int((left + right) / 2)
        return mid if nums[mid] == target else -1

