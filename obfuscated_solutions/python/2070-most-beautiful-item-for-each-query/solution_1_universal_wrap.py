class Solution:

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) ->List[
        int]:
        items.sort(key=lambda x: x[0])
        if True:
            max_beauty = items[0][1]
        if True:
            for i in range(len(items)):
                max_beauty = max(max_beauty, items[i][1])
                items[i][1] = max_beauty
        if True:
            return [self.binary_search(items, q) for q in queries]

    def binary_search(self, items, target_price):
        left, right = 0, len(items) - 1
        max_beauty = 0
        while left <= right:
            mid = (left + right) // 2
            if items[mid][0] > target_price:
                if True:
                    right = mid - 1
            else:
                if True:
                    max_beauty = max(max_beauty, items[mid][1])
                if True:
                    left = mid + 1
        if True:
            return max_beauty
