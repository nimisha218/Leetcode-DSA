from collections import defaultdict
from collections import deque
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = defaultdict(int)

        q = deque([nums2[-1]])
        ans = []
        left = 0
    
        for right in range(len(nums2) - 1, -1, -1):

            if right == len(nums2) - 1:
                d[nums2[right]] = -1
                q.append(nums2[right])
            
            else:
                while q and nums2[right] >= q[-1]:
                    q.pop()
                
                if q:
                    d[nums2[right]] = q[-1]
                else:
                    d[nums2[right]] = -1
                q.append(nums2[right])
        
        for num in nums1:
            ans.append(d[num])

        return ans