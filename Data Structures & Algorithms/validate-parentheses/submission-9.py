class Solution:
    def isValid(self, s: str) -> bool:
        close2open = {")":"(", 
                      "}":"{", 
                      "]":"["}
        stack = []

        for c in s:
            if len(stack) != 0 and (c == ")" or c == "}" or c == "]"):
                top = stack[-1]
                if close2open[c] == top:
                    stack.pop()
                    continue
            stack.append(c)

        return len(stack) == 0