class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in closers:
                if not stack or stack.pop() != closers[c]:
                    return False
            else:
                stack.append(c)
        return not stack