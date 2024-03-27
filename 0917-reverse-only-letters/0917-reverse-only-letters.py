class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        s_string = []

        for ch in s:
            s_string.append(ch)

        left = 0
        right = len(s) -1 

        while left < right and left < len(s_string) and right > 0:
            if s_string[left].isalpha() and s_string[right].isalpha():
                s_string[left], s_string[right] = s_string[right], s_string[left]
                left += 1
                right -= 1
            elif s_string[left].isalpha():
                right -= 1
            else:
                left += 1

        return "".join(s_string)