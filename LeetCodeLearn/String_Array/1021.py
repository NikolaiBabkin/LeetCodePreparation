class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = ''
        counter = 0
        it1 = 0
        for it2 in range(len(S)):
            counter += 1 if S[it2] == '(' else -1
            if counter == 0:
                res += S[(it1 + 1): it2]
                it1 = it2 + 1

        return res


if __name__ == '__main__':
    s = Solution()
    inp = "(()())(())"
    out = "()()()"
    print(f'Test 1: {s.removeOuterParentheses(inp) == out}')

    inp = "(()())(())(()(()))"
    out = "()()()()(())"
    print(f'Test 1: {s.removeOuterParentheses(inp) == out}')

    inp = "()()"
    out = ""
    print(f'Test 1: {s.removeOuterParentheses(inp) == out}')