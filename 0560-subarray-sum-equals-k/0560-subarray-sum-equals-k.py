from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = curr = 0
        counts = defaultdict(int)
        counts[0] = 1

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1
        
        return ans
