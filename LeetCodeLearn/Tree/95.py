# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        """
        https: // en.wikipedia.org / wiki / Catalan_number
        Time Complexity: O(C(n))
        Space Complexity: O(C(n))
        """
        def generator(low, upper):
            if len(arr[low: upper]) == 0:
                yield None
            for i in range(low, upper):
                for left in generator(low, i):
                    for right in generator(i + 1, upper):
                        yield TreeNode(arr[i], left, right)

        arr = list(range(1, n + 1))
        return [root for root in generator(0, n)]


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))
