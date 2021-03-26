class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """

        adj_list = [[[], 0] for _ in range(numCourses)]
        for v_in, v_out in prerequisites:
            adj_list[v_out][0].append(v_in)
            adj_list[v_in][1] += 1

        res = []
        stack = []
        for course in range(numCourses):
            if adj_list[course][1] > 0:
                continue
            res.append(course)
            stack.append(course)

        cnt_deleted = 0
        while stack:
            course = stack.pop()
            for dep_course in adj_list[course][0]:
                adj_list[dep_course][1] -= 1
                cnt_deleted += 1
                if adj_list[dep_course][1] == 0:
                    stack.append(dep_course)
                    res.append(dep_course)

        if cnt_deleted != len(prerequisites):
            return []
        return res
