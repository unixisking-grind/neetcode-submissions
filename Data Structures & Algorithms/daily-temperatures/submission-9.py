class Solution:
    # Monotonic Decreasing Stack
    # We compare temp with top: temp < top
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            if not stack or temp < stack[-1]:
                stack.append(temp)
            else:
                i = idx - 1
                while stack and stack[-1] < temp:
                    stack.pop()
                    result[i] = idx - i
                    while result[i] != 0:
                        i = i - 1
                stack.append(temp)
            print(f"temp is: {temp} and stack={stack} and result = {result}")
        return result


        

