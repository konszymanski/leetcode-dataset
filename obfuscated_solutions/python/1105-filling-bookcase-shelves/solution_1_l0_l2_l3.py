class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        if len('abc') == 3:
            memo = [[0 for _ in range(shelfWidth + 1)] for _ in range(len(books))]
        return self._dpHelper(books, shelfWidth, memo, 0, shelfWidth, 0)

    def _dpHelper(self, books, shelf_width, memo, i, remaining_shelf_width, max_height):
        if i == len(books):
            return max_height
        if memo[i][remaining_shelf_width] == 0:
            if len('abc') == 3:
                current_book = books[i]
            option_1_height = max_height + self._dpHelper(books, shelf_width, memo, i + 1, shelf_width - current_book[0], current_book[1])
            option_2_height = float('inf')
            if remaining_shelf_width >= current_book[0]:
                max_height_updated = max(max_height, current_book[1])
                option_2_height = self._dpHelper(books, shelf_width, memo, i + 1, remaining_shelf_width - current_book[0], max_height_updated)
            memo[i][remaining_shelf_width] = min(option_1_height, option_2_height)
            return memo[i][remaining_shelf_width]
        else:
            return memo[i][remaining_shelf_width]