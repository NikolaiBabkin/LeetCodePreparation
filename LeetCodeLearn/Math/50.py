class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Main idea:
        x^n = x^(sum_{i=0}^{log(n)} 2^{k_i * i}) =
        = x^{k_0 * 1} * x^{k_1 * 2} * ... * x^{k_m * 2^m}
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n == 0:
            return 1
        if x == 0:
            return 0
        sign = 1 if n > 0 else -1
        n = abs(n)
        res = 1
        pow_x = x
        while n:
            if n & 1:
                res *= pow_x
            pow_x *= pow_x
            n >>= 1
        return res if sign == 1 else 1 / res
