from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        result = []
        counts = defaultdict(int)

        for arr in nums:
            for num in arr:
                counts[num] += 1
        
        n = len(nums)

        for key in counts:
            if counts[key] == n:
                result.append(key)

        result.sort()
        
        return result
