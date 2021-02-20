# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        Time Complexity: O(n - m)
        Space Complexity: O(n - m)
        """
        self.dfs(robot, 0, 0, 0, 1, set())

    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        for k in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x

    def cleanRoom_2(self, robot):
        """
        Time Complexity: O(n - m)
        Space Complexity: O(n - m)
        """
        def backtrack():
            robot.clean()
            visited.add((pos[1][0] - pos[1][2], pos[1][1] - pos[1][3]))
            for direction in range(4):
                if is_visited(direction):
                    continue
                if place(direction):
                    pos[1][direction] += 1
                    backtrack()
                    remove(direction)
                    pos[1][direction] -= 1

        def remove(direction):
            place((direction + 2) % 4)

        def place(direction):
                turn_to(direction)
                return robot.move()

        def turn_to(direction):
            if direction == (pos[0] + 1) % 4:
                robot.turnRight()
                pos[0] = (pos[0] + 1) % 4
            else:
                while direction != pos[0]:
                    robot.turnLeft()
                    pos[0] -= 1
                    if pos[0] == -1:
                        pos[0] = 3

        def is_visited(direction):
                to_go = pos[1][:]
                to_go[direction] += 1
                to_go_coord = (to_go[0] - to_go[2], to_go[1] - to_go[3])
                return to_go_coord in visited

        visited = set()
        # (facing, ['up', right, 'down', left])
        # facing: 0 - up, 1 - right, 2 - down, 3 - left
        pos = [0, [0] * 4]
        backtrack()

