class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        obj = {}
        # Monotonic strictly decreasing stack
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if len(stack) == 0 or temperatures[stack[-1]] > temp:
                stack.append(i)
            else:
                while len(stack) > 0 and temp > temperatures[stack[-1]]:
                    element = stack.pop()
                    result[element] = i - element
                stack.append(i)
            print(stack)

        
        while len(stack) != 0:
            # Since they were not popped before that means we couldn't
            # find a greater element before finishing up the array
            # wich means we set their values to 0 in the result array
            element = stack.pop()
            print(f"element = {element}")
            result[element] = 0

        return result





        