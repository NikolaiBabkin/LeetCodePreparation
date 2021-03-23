class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        bulls = cows = 0
        counter = dict()
        for num in secret:
            if num in counter:
                counter[num][0] += 1
            else:
                counter[num] = [1,0]

        for num in guess:
            if num in counter:
                counter[num][1] += 1
            else:
                counter[num] = [0, 1]

        for key, value in counter.items():
            cows += min(value)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1

        cows -= bulls

        return str(bulls) + 'A' + str(cows) + 'B'
