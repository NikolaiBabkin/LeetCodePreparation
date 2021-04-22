class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtracking(i):
            curr.append(num[i])
            if i == len(num) - 1:
                sub_res = ''.join(curr)
                if eval(sub_res) == target:
                    res.append(sub_res)
                curr.pop()

                return

            for sep in ['+', '-', '*', '']:
                if num[i] == '0' and (len(curr) == 1 or curr[-2] != '') and sep == '':
                    continue
                curr.append(sep)
                backtracking(i + 1)
                curr.pop()
            curr.pop()


        res = []
        curr = []
        backtracking(0)
        return res

