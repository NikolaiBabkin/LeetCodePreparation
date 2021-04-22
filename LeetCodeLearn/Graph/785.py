class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Time Complexity: O(V+E)
        Space Complexity: O(V)
        """
        colours = [0] * len(graph)
        for v in range(len(graph)):
            if colours[v] != 0:
                continue

            colours[v] = 1
            stack = [v]
            while stack:
                v = stack.pop()
                for v_adj in graph[v]:
                    if colours[v_adj] == 0:
                        colours[v_adj] = - colours[v]
                        stack.append(v_adj)
                    elif colours[v_adj] == colours[v]:
                        return False

        return True

