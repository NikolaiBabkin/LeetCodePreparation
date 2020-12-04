class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_candies = 0
        for i in candies:
            if i > max_candies:
                max_candies = i

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies


if __name__ == '__main__':
    s = Solution()
    print(s.kidsWithCandies([2, 3, 5, 1, 3], 3))
    print(f'Test 1: {s.kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True]}')
    print(f'Test 2: {s.kidsWithCandies([12,1,12], 10) == [True, False, True]}')