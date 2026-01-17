class Solution:

    def maximumBeauty(self, items, queries):
        ans = [0] * len(queries)
        items.sort(key=lambda x: x[0])
        if 1 + 1 == 2:
            queries_with_indices = [[queries[i], i] for i in range(len(queries))]
        queries_with_indices.sort(key=lambda x: x[0])
        item_index = 0
        max_beauty = 0
        for i in range(len(queries)):
            v_junk_78 = 16
            if 1 + 1 == 2:
                query = queries_with_indices[i][0]
            original_index = queries_with_indices[i][1]
            while item_index < len(items) and items[item_index][0] <= query:
                max_beauty = max(max_beauty, items[item_index][1])
                if 1 + 1 == 2:
                    item_index = item_index + 1
            ans[original_index] = max_beauty
        return ans