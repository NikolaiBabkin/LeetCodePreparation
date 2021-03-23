class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def collision():
            if stack[-2] > 0 and stack[-1] < 0:
                return True
            return False

        def solve_collision():
            if abs(stack[-2]) == abs(stack[-1]):
                stack.pop()
                stack.pop()
            elif abs(stack[-2]) > abs(stack[-1]):
                stack.pop()
            else:
                stack[-2] = stack[-1]
                stack.pop()

        stack = []
        for astr in asteroids:
            stack.append(astr)
            if len(stack) < 2 or not collision():
                continue

            while len(stack) > 1 and collision():
                solve_collision()

        return stack


