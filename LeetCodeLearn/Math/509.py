class Solution:
    def fib_characteristic(self, n: int) -> int:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        l1 = (1 + 5**0.5) / 2
        l2 = (1 - 5 ** 0.5) / 2
        return int((l1**n - l2**n) / 5**0.5)

    def fib(self, n: int) -> int:
        """
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        def matr_mult(L, R):
            res = [[0, 0], [0, 0]]
            res[0][0] = L[0][0] * R[0][0] + L[0][1] * R[1][0]
            res[0][1] = L[0][0] * R[0][1] + L[0][1] * R[1][1]
            res[1][0] = L[1][0] * R[0][0] + L[1][1] * R[1][0]
            res[1][1] = L[1][0] * R[0][1] + L[1][1] * R[1][1]
            return res

        E = [[1, 0], [0, 1]]
        A = [[1, 1], [1, 0]]
        F_0 = 0
        F_1 = 1
        if n == 0:
            return F_0
        if n == 1:
            return F_1
        power = n - 1
        B = E
        tmp_B = A
        while power:
            m_k = power & 1
            power >>= 1
            if m_k:
                B = matr_mult(B, tmp_B)
            tmp_B = matr_mult(tmp_B, tmp_B)

        return B[0][0] * F_1 + B[0][1] * F_0


if __name__ == '__main__':
    s = Solution()
    print(s.fib_characteristic(4))