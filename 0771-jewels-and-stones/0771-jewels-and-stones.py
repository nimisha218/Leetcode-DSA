class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels_list = []
        for jewel in jewels:
            jewels_list.append(jewel)

        ans = 0
        
        for stone in stones:
            if stone in jewels_list:
                ans += 1
        
        return ans

        