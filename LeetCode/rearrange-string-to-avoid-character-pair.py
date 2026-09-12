class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        front = back = ''
        for ch in s:
            if ch == y:
                front = front+ch
            else:
                back = back+ch
        return front+back