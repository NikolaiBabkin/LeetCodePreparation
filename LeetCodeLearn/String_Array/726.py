class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def get_mult(idx, end):
            num = ['0']
            while idx < end and ord('0') <= ord(formula[idx]) <= ord('9'):
                num.append(formula[idx])
                idx += 1

            return max(1, int(''.join(num))), idx

        def count_atoms(start, end):
            counter = dict()
            p1 = start
            while p1 < end:
                if parentheses and p1 == parentheses[-1][0]:
                    sub_start = parentheses[-1][0] + 1
                    sub_end = parentheses[-1][1]
                    parentheses.pop()
                    sub_counter = count_atoms(sub_start, sub_end)
                    mult, p1 = get_mult(sub_end + 1, end)
                    for k, v in sub_counter.items():
                        if k in counter:
                            counter[k] += mult * v
                        else:
                            counter[k] = mult * v
                else:
                    p2 = p1 + 1
                    while p2 < end and 'a' <= formula[p2] <= 'z':
                        p2 += 1

                    atom = formula[p1: p2]
                    p1 = p2
                    while p2 < end and '0' <= formula[p2] <= '9':
                        p2 += 1

                    cnt = int(formula[p1: p2]) if p2 - p1 != 0 else 1
                    if atom in counter:
                        counter[atom] += cnt
                    else:
                        counter[atom] = cnt
                    p1 = p2
            return counter


        parentheses = []
        stack = []
        for idx, ch in enumerate(formula):
            if ch in ['(', ')']:
                if stack and stack[-1][0] + ch == '()':
                    parentheses.append((stack[-1][1], idx))
                    stack.pop()
                else:
                    stack.append((ch, idx))

        parentheses.sort(key = lambda x: x[0], reverse=True)

        counter = count_atoms(0, len(formula))
        counter = [(k, v) for k, v in counter.items()]
        counter.sort(key=lambda x: x[0])
        res = []
        for k, v in counter:
            if v > 1:
                res.append(k + str(v))
            else:
                res.append(k)
        return ''.join(res)

