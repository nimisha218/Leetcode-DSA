from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        def get_freq(arr):
            d = defaultdict(int)
            for val in arr:
                d[val] += 1
            return d
        
        r = get_freq(ransomNote)
        m = get_freq(magazine)

        for key in r:
            if r[key] > m[key]:
                return False
        return True

