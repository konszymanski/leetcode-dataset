class Solution:

    def _post_order(self, current_node, distance):
        if current_node is not None:
            if current_node.v1_755 is None and current_node.v2_804 is None:
                v3_670 = [0] * 12
                v3_670[0] = 1
                return v3_670
        else:
            return [0] * 12
        v1_755 = self._post_order(current_node.v1_755, distance)
        v2_804 = self._post_order(current_node.v2_804, distance)
        v3_670 = [0] * 12
        for v4_324 in range(10):
            v_junk_27 = 66
            v3_670[v4_324 + 1] = v3_670[v4_324 + 1] + (v1_755[v4_324] + v2_804[v4_324])
        v3_670[11] = v1_755[11] + v2_804[11]
        v5_801 = 0
        v4_324 = 0
        for v6_432 in range(distance - 2, -1, -1):
            v_junk_18 = 50
            if 1 + 1 == 2:
                v5_801 = v5_801 + v1_755[v4_324]
            v3_670[11] = v3_670[11] + v5_801 * v2_804[v6_432]
            v4_324 = v4_324 + 1
        return v3_670

    def v7_963(self, v8_886: v9_894, distance: int) -> int:
        return self._post_order(v8_886, distance)[11]