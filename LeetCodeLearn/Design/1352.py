class ProductOfNumbers:
    """
    Time Complexity: O(1)
    Space Complexity: O(n)
    """
    def __init__(self):
        self.products = [1] # [3, 3, 6, 30, 120]
        self.last_zero = -1 # 1

    def add(self, num):
        if num == 0:
            self.last_zero = len(self.products)
            if len(self.products) == 0:
                self.products = [1]
            else:
                self.products.append(self.products[-1])
        else:
            if len(self.products) == 0:
                self.products = [num]
            else:
                self.products.append(self.products[-1] * num)

    def getProduct(self, k):
        if k >= len(self.products) - self.last_zero:
            return 0

        return self.products[-1] // self.products[-k-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)