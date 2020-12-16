class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        a_dict = dict()
        for i in A:
            if i in a_dict:
                return i
            else:
                a_dict[i] = 1
        return None

    def repeatedNTimes_space_effective(self, A: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(4, len(A)):
            if A[i-4] == A[i-3]:
                return A[i-4]
            if A[i-4] == A[i-2]:
                return A[i-4]
            if A[i-4] == A[i-1]:
                return A[i-4]
            if A[i-3] == A[i-2]:
                return A[i-3]
            if A[i-3] == A[i-1]:
                return A[i-3]
            if A[i-1] == A[i-2]:
                return A[i-1]
        return None
