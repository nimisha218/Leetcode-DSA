class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        for c in s:
            if stack:
                if c.lower() == stack[-1].lower():
                    if c.islower() and stack[-1].isupper():
                        stack.pop()
                        continue
                    elif c.isupper() and stack[-1].islower():
                        stack.pop()
                        continue
                    else:
                        stack.append(c)
                        continue   
            
            stack.append(c)
        
        return "".join(stack)