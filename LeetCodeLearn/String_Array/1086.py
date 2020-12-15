class Solution:
    def highFive(self, items):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def count_sort(arr, min_val, max_val):
            helper = [0] * (max_val - min_val + 1)
            for i in arr:
                helper[i - min_val] += 1

            sorted_arr = [0] * len(arr)
            it = 0
            for i in range(len(helper)):
                if helper[i]:
                    sorted_arr[it: (it + helper[i])] = [i + min_val] * helper[i]
                    it += helper[i]
            return sorted_arr

        students = dict()
        for stud_id, score in items:
            if stud_id in students:
                students[stud_id].append(score)
            else:
                students[stud_id] = [score]

        for stud_id in students:
            sorted_scores = count_sort(students[stud_id], 0, 100)
            students[stud_id] = sum(sorted_scores[-5:]) // 5

        res = [0] * len(students)
        sorted_id = count_sort(students.keys(), 1, 1000)
        for j, stud_id in enumerate(sorted_id):
            res[j] = [stud_id, students[stud_id]]

        return res


if __name__ == '__main__':
    s = Solution()
    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    output = [[1,87],[2,88]]
    print(f'Test 1: {s.highFive(items) == output}')

    items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
    output = [[1,100],[7,100]]
    print(f'Test 1: {s.highFive(items) == output}')