class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]

        seen = {"".join(morse[ord(c) - ord('a')] for c in word)
                for word in words}

        return len(seen)



if __name__ == '__main__':
    s = Solution()
    res = s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(res)