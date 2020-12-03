class Solution:
    def toLowerCase(self, str: str) -> str:
        diff = ord('a') - ord('A')
        is_upper = lambda x: 'A' <= x <= 'Z'
        to_lowet = lambda x: chr(ord(x) + diff)
        return ''.join(to_lowet(i) if is_upper(i) else i for i in str)

if __name__ == "__main__":
    s = Solution()
    print(s.toLowerCase("LOV@ELY"))