class Solution:
    def arraysIntersection_brute_force(self, arr1, arr2, arr3):
        helper = [0] * 2000
        for itm in arr1:
            helper[itm - 1] += 1
        for itm in arr2:
            helper[itm - 1] += 1
        for itm in arr3:
            helper[itm - 1] += 1

        cnt = 0
        for itm in helper:
            if itm == 3:
                cnt += 1
        res = [0] * cnt
        it = 0
        for i in range(len(helper)):
            if helper[i] == 3:
                res[it] = i + 1
                it += 1

        return res

    def arraysIntersection_optimal(self, arr1, arr2, arr3):
        pass


if __name__ == '__main__':
    s = Solution()
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,5,7,9]
    arr3 = [1,3,4,5,8]
    print(s.arraysIntersection(arr1, arr2, arr3))