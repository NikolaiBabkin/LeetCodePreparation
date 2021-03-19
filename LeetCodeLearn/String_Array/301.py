class Solution:
    def removeInvalidParentheses(self, s: str):
        """
        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        def to_delete(arr) -> dict:
            stack = []
            for ch in arr:
                if ch in ['(', ')']:
                    if stack and stack[-1] + ch == '()':
                        stack.pop(-1)
                    else:
                        stack.append(ch)

            res = {'(': 0, ')': 0}
            for ch in stack:
                res[ch] += 1
            return res

        def is_correct(arr):
            for k, v in to_delete(arr).items():
                if v != 0:
                    return False
            return True

        def backtracking(pointer):
            if pointer == len(s):
                if is_correct(curr):
                    res.add(''.join(curr))
            else:
                if s[pointer] in remove:
                    if remove[s[pointer]] > 0:
                        remove[s[pointer]] -= 1
                        backtracking(pointer + 1)
                        remove[s[pointer]] += 1
                curr.append(s[pointer])
                backtracking(pointer + 1)
                curr.pop(-1)

        if not s:
            return []
        s = [ch for ch in s]
        remove = to_delete(s)
        curr = []
        res = set()
        backtracking(0)
        if -1 in res:
            res.remove(-1)
        return list(res)



if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses("()())()"))