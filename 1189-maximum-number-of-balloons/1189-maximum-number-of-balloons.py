from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        b = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        freq = defaultdict(int)
        
        for t in text:
            if t in b:
                freq[t] += 1
        
        count = 0

        while len(freq) == len(b):
            flag = 0
            delete = []
            for key in freq:
                if freq[key] >= b[key]:
                    freq[key] -= b[key]
                else:
                    flag = 1
                    break
            if flag == 1:
                break
            count += 1

        return count