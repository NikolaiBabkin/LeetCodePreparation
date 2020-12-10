class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            j = len(s) - i - 1
            s[i], s[j] = s[j], s[i]
        return s

    def reverse_bitwise(self, s):
        shift = 10
        for i in range(len(s)):
            s[i] = ord(s[i]) << shift

        for i in range(len(s)):
            s[i] = s[i] + (s[len(s) - i - 1] >> shift)

        for i in range(len(s)):
            s[i] = chr(s[i] & ((1 << shift) - 1))

        return s


if __name__ == '__main__':
    s = Solution()
    arr = ["h","e","l","l","o"]
    print(f'Test 1:{s.reverseString(arr) == ["o","l","l","e","h"]}')

    arr = ["H","a","n","n","a","h"]
    print(f'Test 2:{s.reverseString(arr) == ["h","a","n","n","a","H"]}')

    arr = ["h","e","l","l","o"]
    print(f'Test 4:{s.reverseString(arr) == s.reverse_bitwise(arr)}')

    arr = ["H","a","n","n","a","h"]
    print(f'Test 5:{s.reverseString(arr) == s.reverse_bitwise(arr)}')