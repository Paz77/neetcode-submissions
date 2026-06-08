class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if stack and (c == ')' or c == '}' or c == ']'):
                top = stack[-1]
                if brackets[c] == top:
                    stack.pop()
                    continue
            stack.append(c)

        return len(stack) == 0