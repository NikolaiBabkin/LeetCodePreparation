class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        curr_max = -1
        for i in range(len(arr) - 1, -1, -1):
            curr_elem = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, curr_elem)
        return arr
