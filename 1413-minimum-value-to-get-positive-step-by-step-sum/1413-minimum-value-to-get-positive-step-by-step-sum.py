class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        # Compute the prefix array
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        min_val = min(prefix)

        if min_val < 0:
            return abs(min_val) + 1
        
        else:
            return 1
