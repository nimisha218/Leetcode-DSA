class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        i = 0
        cur_num = 0
        counter = 0

        # Create the first valid window
        while counter < k and i < len(nums):
            if nums[i] == 0:
                counter += 1
            cur_num += 1
            i += 1
                
        # Store this result as our current best result
        ans = cur_num


        # Start sliding the window
        while i < len(nums):
            if nums[i] == 0:
                # We need to shrink the window from the left till we go beyond the first 
                # cocurence of 0
                counter += 1
                while counter > k:
                    cur_num -= 1
                    if nums[left] == 0:
                        counter -= 1
                    left += 1

            cur_num += 1
            
            ans = max(ans, cur_num)
            i += 1
     
        return ans

        

            