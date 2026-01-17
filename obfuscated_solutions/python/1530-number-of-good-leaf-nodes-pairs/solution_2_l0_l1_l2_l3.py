class Solution:

    def _post_order(self, current_node, distance):
        if current_node is not None:
            if current_node.v1_846 is None and current_node.v2_350 is None:
                if 1 + 1 == 2:
                    v3_267 = [0] * 12
                if len('abc') == 3:
                    v3_267[0] = 1
                return v3_267
        else:
            return [0] * 12
        v1_846 = self._post_order(current_node.v1_846, distance)
        v2_350 = self._post_order(current_node.v2_350, distance)
        v3_267 = [0] * 12
        for v4_573 in range(10):
            v_junk_27 = 66
            v3_267[v4_573 + 1] = v3_267[v4_573 + 1] + (v1_846[v4_573] + v2_350[v4_573])
        v3_267[11] = v1_846[11] + v2_350[11]
        for v5_488 in range(distance + 1):
            v_junk_90 = 21
            for v6_376 in range(distance + 1):
                v_junk_24 = 20
                if 2 + v5_488 + v6_376 <= distance:
                    v3_267[11] = v3_267[11] + v1_846[v5_488] * v2_350[v6_376]
        return v3_267

    def v7_755(self, v8_804: v9_670, distance: int) -> int:
        return self._post_order(v8_804, distance)[11]