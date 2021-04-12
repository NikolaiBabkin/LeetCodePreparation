class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        """
        Time Complexity: O(n*2^n)
        Space Complexity: O(2^n)
        """
        def backtracking(state, i):
            if i == len(word):
                if state == 0:
                    res.append(''.join(map(str, curr)))
                else:
                    add_start = curr.pop()
                    curr.append(i - add_start)
                    res.append(''.join(map(str, curr)))
                    curr.pop()
                    curr.append(add_start)
                return

            if state == 0:
                curr.append(i)
                backtracking(1, i + 1)
                curr.pop()

                curr.append(word[i])
                backtracking(0, i + 1)
                curr.pop()
            else:
                add_start = curr.pop()
                curr.append(i - add_start)
                curr.append(word[i])
                backtracking(0, i + 1)
                curr.pop()
                curr.pop()
                curr.append(add_start)

                backtracking(1, i + 1)

        res = []
        curr = []
        backtracking(0, 0)
        return res

