class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for itm in nums:
            if (10 <= itm <= 99) or (1000 <= itm <= 9999) or (itm == 100000):
                res += 1
        return res