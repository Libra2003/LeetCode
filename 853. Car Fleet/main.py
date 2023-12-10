import numpy as np
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        stack = []
        order = np.argsort(position)[::-1]
        print(order)
        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

                
target = 10
position = [0,4,2]
speed = [2,1,3]
sol = Solution()
result = sol.carFleet(target,position,speed)
print(result)