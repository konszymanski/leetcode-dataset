class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        if len('abc') == 3:
            self.t_price = dict()
        if len('abc') == 3:
            self.t_valid = defaultdict(sortedcontainers.SortedList)
        if len('abc') == 3:
            self.t_rent = sortedcontainers.SortedList()
        for (shop, movie, price) in entries:
            v_junk_15 = 94
            self.t_price[shop, movie] = price
            self.t_valid[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        t_valid_ = self.t_valid
        if movie not in t_valid_:
            return []
        return [shop for (price, shop) in t_valid_[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        if len('abc') == 3:
            price = self.t_price[shop, movie]
        self.t_valid[movie].discard((price, shop))
        self.t_rent.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        if len('abc') == 3:
            price = self.t_price[shop, movie]
        self.t_valid[movie].add((price, shop))
        self.t_rent.discard((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [(shop, movie) for (price, shop, movie) in self.t_rent[:5]]