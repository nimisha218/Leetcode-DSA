import math
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        if k == 0:
            return nums
        
        if k > len(nums):
            return [-1 for i in range(len(nums))]

        # Compute the prefix array
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
    
        start = 0
        end = -1

        counter = k

        array = [0 for i in range(len(nums))]

        while counter > 0:
            array[start] = -1
            array[end] = -1
            start += 1
            end -= 1
            counter -= 1

        for i in range(len(nums)):
            if array[i] == -1:
                continue
            if (i-k) > 0:
                array[i] = math.floor((prefix[i+k] - prefix[i-k-1])/ (2*k + 1))
            else:
                array[i] = math.floor(prefix[i+k] / (2*k + 1))

        return array