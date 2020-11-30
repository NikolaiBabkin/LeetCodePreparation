'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Example 3:
Input: J = "", S = "ZaBc"
Output: 0

Example 4:
Input: J = "z", S = ""
Output: 0



Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''


class Solution:
    def numJewelsInStones_slow(self, J: str, S: str) -> int:
        my_stones = {}
        for s in S:
            if s not in my_stones.keys():
                my_stones[s] = 1
            else:
                my_stones[s] += 1

        res = 0
        for s in J:
            if s in my_stones.keys():
                res += my_stones[s]

        return res

    def numJewelsInStones(self, J: str, S: str) -> int:
        setJ = set(J)
        res = sum(s in setJ for s in S)
        return res


if __name__ == "__main__":
    s = Solution()
    J = "z"
    S = ""
    print(s.numJewelsInStones(J, S))