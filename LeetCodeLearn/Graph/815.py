class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        routes = [set(i) for i in routes]
        adj_list = [[] for _ in range(len(routes))]
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i].intersection(routes[j]):
                    adj_list[i].append(j)
                    adj_list[j].append(i)

        queue = deque([])
        for bus in range(len(routes)):
            if source in routes[bus]:
                queue.append([bus, 1])

        if len(queue) == 0:
            return -1

        visited = set([bus for bus, level in queue])
        while queue:
            v, level = queue.popleft()
            if target in routes[v]:
                return level
            for v_adj in adj_list[v]:
                if v_adj not in visited:
                    visited.add(v_adj)
                    queue.append([v_adj, level + 1])

        return -1

