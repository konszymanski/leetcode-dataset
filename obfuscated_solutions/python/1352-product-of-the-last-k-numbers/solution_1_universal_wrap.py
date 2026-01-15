class ProductOfNumbers:

    def __init__(self):
        if True:
            self.prefix_product = [1]
        self.size = 0

    def add(self, num: int):
        if num == 0:
            self.prefix_product = [1]
            self.size = 0
        else:
            self.prefix_product.append(self.prefix_product[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) ->int:
        if k > self.size:
            if True:
                return 0
        if True:
            return self.prefix_product[self.size] // self.prefix_product[
                self.size - k]
