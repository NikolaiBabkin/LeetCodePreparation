class Solution:
    def sortArrayByParity(self, arr):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        it1 = 0
        it2 = len(arr) - 1
        while it1 < it2:
            if (arr[it1] % 2 == 1) and (arr[it2] % 2 == 0):
                arr[it1], arr[it2] = arr[it2], arr[it1]
                it1 += 1
                it2 -= 1
            if (arr[it1] % 2 == 0) and (arr[it2] % 2 == 0):
                it1 += 1
            if (arr[it1] % 2 == 1) and (arr[it2] % 2 == 1):
                it2 -= 1
            if (arr[it1] % 2 == 0) and (arr[it2] % 2 == 1):
                it1 += 1
                it2 -= 1

        return arr

if __name__ == '__main__':
    s = Solution()
    A = [3,1,2,4]
    print(s.sortArrayByParity(A))