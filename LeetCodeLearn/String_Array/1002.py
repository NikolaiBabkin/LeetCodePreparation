class Solution:
    def commonChars(self, arr: List[str]) -> List[str]:
        counter = dict()
        for s in arr:
            for ch, cnt in collections.Counter(s).items():
                if ch in counter:
                    counter[ch][0] = min(counter[ch][0], cnt)
                    counter[ch][1] += 1
                else:
                    counter[ch] = [cnt, 1]

        res = [[ch] * cnt[0] for ch, cnt in counter.items() if cnt[1] == len(arr)]
        return [ch for sub in res for ch in sub]

    def commonChars_2(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())

