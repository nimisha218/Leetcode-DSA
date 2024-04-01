from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        d = defaultdict(list)

        ans = float("inf")

        for i in range(len(cards)):
            d[cards[i]].append(i)

        for key in d:
            arr = d[key]

            if len(d[key]) >= 2:
                for i in range(len(d[key]) - 1):
                    if abs(arr[i] - arr[i + 1]) + 1 <= ans:
                        ans = abs(arr[i] - arr[i + 1]) + 1

        if ans < float("inf"):
            return ans
        else:
            return -1
           