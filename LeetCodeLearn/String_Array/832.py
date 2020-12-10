class Solution:
    def flipAndInvertImage(self, A):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def flip_invert_list(l):
            return [1 * (i == 0) for i in l[::-1]]

        for col in range(len(A)):
            A[col] = flip_invert_list(A[col])
        return A


if __name__ == '__main__':
    s = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    output = [[1,0,0],[0,1,0],[1,1,1]]
    print(f'Test 1: {s.flipAndInvertImage(A) == output}')


    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    output = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    print(f'Test 2: {s.flipAndInvertImage(A) == output}')