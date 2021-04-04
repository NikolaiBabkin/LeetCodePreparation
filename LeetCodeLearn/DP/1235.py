from functools import lru_cache


class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        @lru_cache(None)
        def dp(k):
            if k >= len(startTime):
                return 0
            k_next = get_next(k)
            res = max(profit[k] + dp(k_next), dp(k + 1))
            return res

        def get_next(k):
            target = endTime[k]
            l = k
            if l + 1 >= len(startTime):
                return len(startTime)
            r = len(startTime) - 1
            while l + 1 < r:
                m = l + (r - l) // 2
                if startTime[m] >= target:
                    r = m
                else:
                    l = m
            if startTime[r] >= target:
                return r
            return r + 1

        tmp = [(startTime.pop(), endTime.pop(), profit.pop()) for _ in range(len(startTime))]
        tmp.sort(key=lambda x: x[0])
        for s, e, p in tmp:
            startTime.append(s)
            endTime.append(e)
            profit.append(p)

        k = get_next(0)
        res = max(profit[0] + dp(k), dp(1))
        return res


if __name__ == '__main__':
    s = Solution()
    startTime = [4, 2, 4, 8, 2]
    endTime = [5, 5, 5, 10, 8]
    profit = [1, 2, 8, 10, 4]
    print(s.jobScheduling(startTime,endTime,profit))