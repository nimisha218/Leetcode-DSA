class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        result = []

        for index, num in enumerate(nums):
            
            if (target - num) not in d:
                d[num] = index
            else:
                result.append(d[target - num])
                result.append(index)
                
        return result

        