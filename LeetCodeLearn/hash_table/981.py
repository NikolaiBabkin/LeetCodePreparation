class TimeMap:
    def __init__(self):
        self.data = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([timestamp, value])
        else:
            self.data[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data or timestamp < self.data[key][0][0]:
            return  ''

        l = 0
        r = len(self.data[key])
        while l + 1 < r:
            m = l + (r - l) // 2
            if timestamp < self.data[key][m][0]:
                r = m
            else:
                l = m

        return self.data[key][l][1]
