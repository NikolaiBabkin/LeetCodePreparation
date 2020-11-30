'''
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:
Input: "aeiou"
Output: ""


Note:
S consists of lowercase English letters only.
1 <= S.length <= 1000
'''

class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = ''
        for s in S:
            if s not in vowels:
                res += s

        return res


if __name__ == "__main__":
    s = Solution()
    print("" == s.removeVowels("aeiou"))