from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        output = []

        l = r = 0

        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            queue.append(r)

            # Check is left is outside the window
            if l > queue[0]:
                queue.popleft()
            
            # Check is valid window size
            if (r + 1) >= k:
                output.append(nums[queue[0]])
                l += 1
            
            r += 1
        
        return output

        

            
    
    
        print("First window: ", stack)

        return []
        