class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        adj_list = [False] * numCourses
        for v_in, v_out in prerequisites:
            if not adj_list[v_in]:
                adj_list[v_in] = [set(), 1]
            else:
                adj_list[v_in][1] += 1

            if not adj_list[v_out]:
                adj_list[v_out] = [{v_in}, 0]
            else:
                adj_list[v_out][0].add(v_in)


        queue = deque()
        for v in range(numCourses):
            if adj_list[v] and adj_list[v][1] == 0:
                queue.append(v)

        deleted_edges = 0
        while queue:
            v = queue.popleft()
            for adj_v in adj_list[v][0]:
                adj_list[adj_v][1] -= 1
                deleted_edges += 1
                if adj_list[adj_v][1] == 0:
                    queue.append(adj_v)

        if deleted_edges == len(prerequisites):
            return True

        return False
