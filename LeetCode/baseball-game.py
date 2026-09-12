class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        for i in operations:
            if is_integer(i):
                stack.append(int(i))
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == '+':
                stack.append(stack[-1]+stack[-2])
        return sum(stack)