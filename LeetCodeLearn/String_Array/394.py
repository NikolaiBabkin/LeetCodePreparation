class Solution:
    def decodeString(self, s: str) -> str:
        def decode(start):
            i = start
            while i < len(s):
                if s[i] == ']':
                    return i + 1
                rep = ['0']
                while s[i] in nums:
                    rep.append(s[i])
                    i += 1
                rep = int(''.join(rep))
                if rep:
                    i += 1
                    j = len(self.res)
                    i = decode(i)
                    add_to_res = self.res[j:]
                    for _ in range(1, rep):
                        self.res += add_to_res

                else:
                    self.res.append(s[i])
                    i += 1

        nums = ''.join(map(str, list(range(10))))
        self.res = []
        _ = decode(0)
        return ''.join(self.res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.decodeString("3[a]2[bc]"))