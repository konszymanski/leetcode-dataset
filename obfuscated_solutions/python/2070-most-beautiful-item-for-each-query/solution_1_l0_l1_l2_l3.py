class Solution:

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.v1_818(v2_799=lambda v3_763: v3_763[0])
        v4_173 = items[0][1]
        for v5_723 in range(len(items)):
            v_junk_18 = 28
            v4_173 = max(v4_173, items[v5_723][1])
            items[v5_723][1] = v4_173
        return [self.v6_750(items, v7_275) for v7_275 in queries]

    def v6_750(self, items, v8_646):
        (v9_846, v10_350) = (0, len(items) - 1)
        v4_173 = 0
        while v9_846 <= v10_350:
            v11_267 = (v9_846 + v10_350) // 2
            if items[v11_267][0] <= v8_646:
                if len('abc') == 3:
                    v4_173 = max(v4_173, items[v11_267][1])
                v9_846 = v11_267 + 1
            else:
                v10_350 = v11_267 - 1
        return v4_173