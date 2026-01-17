class Solution:
    def _post_order(self, current_node, distance):
        if current_node is None:
            return [0] * 12
        elif current_node.v1_754 is None and current_node.v2_214 is None:
            v3_125 = [0] * 12
            v3_125[0] = 1
            return v3_125
        v1_754 = self._post_order(current_node.v1_754, distance)
        v2_214 = self._post_order(current_node.v2_214, distance)
        v3_125 = [0]  *  12
        for v4_859 in range(10):
            v3_125[v4_859  +  1] += v1_754[v4_859]  +  v2_214[v4_859]
        v3_125[11] = v1_754[11]  +  v2_214[11]
        v5_381 = 0
        v4_859 = 0
        for v6_350 in range(distance - 2, -1, -1):
            v5_381  +=  v1_754[v4_859]
            v3_125[11]  +=  v5_381  *  v2_214[v6_350]
            v4_859  +=  1
        return v3_125
    def v7_328(self, v8_242: v9_854, distance: int) -> int:
        return self._post_order(v8_242, distance)[11]
