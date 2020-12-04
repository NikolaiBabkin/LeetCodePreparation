class MovingAverage:
    def __init__(self, size: int):
        self.window = []
        self.window_sum = 0
        self.size = size
        self.count = 0

    def next(self, val: int) -> float:
        """
        Time Complexity: O(1)
        Space Complexity: O(size)
        """
        self.count += 1
        self.window.append(val)
        tail = self.window.pop(0) if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.count, self.size)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
if __name__ == '__main__':
    s = MovingAverage(3)
    values = [1, 10, 3, 5]
    for i in values:
        print(s.next(i))
