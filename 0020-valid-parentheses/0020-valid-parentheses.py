class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for c in s:
            if c in d:
                stack.append(c)
            else:
                if not stack:
                    return False
                top_stack = stack.pop()
                if d[top_stack] != c:
                    return False
        return not stack
