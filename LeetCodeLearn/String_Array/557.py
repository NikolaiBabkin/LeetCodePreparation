class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return ' '.join([word[::-1] for word in s.split(' ')])