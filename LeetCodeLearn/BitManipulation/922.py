class Solution(object):
    def sortArrayByParityII(self, A):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


if __name__ == '__main__':
    s = Solution()
    input = [4,1,1,0,1,0, 1, 0]
    print(s.sortArrayByParityII(input))