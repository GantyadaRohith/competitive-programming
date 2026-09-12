class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        table = {}
        def dp(op, cp):
            # check memo
            if (op, cp) in table:
                return table[(op, cp)]

            if op == n and cp == n:
                return [""]

            res = []

            if op < n:
                for s in dp(op + 1, cp):
                    res.append("(" + s)

            if cp < op:
                for s in dp(op, cp + 1):
                    res.append(")" + s)

            table[(op, cp)] = res
            return res

        return dp(0,0)