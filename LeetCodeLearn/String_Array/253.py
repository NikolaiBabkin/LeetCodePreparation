class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        """
        intervals.sort(key=lambda x: x[0])
        rooms = [intervals[0][1]]
        heapq.heapify(rooms)
        for meeting in intervals[1:]:
            if meeting[0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, meeting[1])

        return len(rooms)

