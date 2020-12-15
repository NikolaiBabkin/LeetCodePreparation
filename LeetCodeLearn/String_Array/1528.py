class Solution:
    def restoreString(self, s, indices):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [0] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    inp = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    print(f'Test 1: {s.restoreString(inp, indices) == "leetcode"}')