# Monotonic Stack Pattern
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums) 
            
        stack = []
        for num in nums:
            if len(stack) == 0:
                stack.append(num)

            elif num > stack[-1]:
                stack.append(num)
            elif num == stack[-1]:
                continue
            else:
                tmp = []
                while len(stack) > 0 and stack[-1] > num:
                    tmp.append(stack.pop())
                stack.append(num)
                while len(tmp) != 0:
                    stack.append(tmp.pop())

        values = []

        prevNum = stack[0]
        count = 0
        for i in range(1, len(stack)):
            if stack[i] - 1 == prevNum:
                prevNum = stack[i]
                count += 1
            else:
                if prevNum == stack[i]:
                    continue

                if count > 0:
                    values.append(count + 1)

                count = 0
                prevNum = stack[i]

        if count > 0:
            values.append(count + 1)

        print("stack:", stack)
        print("values:", values)
        if len(values) > 0:
            return max(values)
        return 1
