class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s: 
            if i in {'(','[','{'}:
                stack.append(i)
            elif not stack and i in '})]':
                return False
            elif i == ')'  and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']'  and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return len(stack) == 0