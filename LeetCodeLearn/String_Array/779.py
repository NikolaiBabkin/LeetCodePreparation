class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if N == 1:
            return 0
        if K == 1:
            return 0
        ancestor = self.kthGrammar(N - 1, (K + 1) // 2)
        if ancestor == 1:
            return int('10'[(K - 1) % 2])
        return int('01'[(K - 1) % 2])
