class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        k_dict = {letter: i for i, letter in enumerate(keyboard)}
        res, current_pos = 0, 0
        for letter in word:
            res += abs(current_pos - k_dict[letter])
            current_pos = k_dict[letter]
        return res


if __name__ == '__main__':
    s = Solution()
    print(f'Test 1: {s.calculateTime("abcdefghijklmnopqrstuvwxyz", "cba") == 4}')
    print(f'Test 2: {s.calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode") == 73}')