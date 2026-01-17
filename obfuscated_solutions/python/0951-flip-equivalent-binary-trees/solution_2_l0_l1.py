class Solution:
    def check_node_values(self, node_1: v1_754, node_2: v1_754)  ->  bool:
        if not node_1 and not node_2:
            return True
        if node_1 and node_2 and node_1.v2_214  ==  node_2.v2_214:
            return True
        return False
    def v3_125(self, v4_859: v1_754, v5_381: v1_754) -> bool:
        v6_350 = []
        v6_350.v7_328((v4_859, v5_381))
        while v6_350:
            node_1, node_2 = v6_350.v8_242()
            if not node_1 and not node_2:
                continue
            if not node_1 or not node_2:
                return False
            if node_1.v2_214 != node_2.v2_214:
                return False
            if self.check_node_values(
                node_1.v9_854, node_2.v9_854
            ) and self.check_node_values(node_1.v10_204, node_2.v10_204):
                v6_350.v7_328((node_1.v9_854, node_2.v9_854))
                v6_350.v7_328((node_1.v10_204, node_2.v10_204))
            elif self.check_node_values(
                node_1.v9_854, node_2.v10_204
            ) and self.check_node_values(node_1.v10_204, node_2.v9_854):
                v6_350.v7_328((node_1.v9_854, node_2.v10_204))
                v6_350.v7_328((node_1.v10_204, node_2.v9_854))
            else:
                return False
        return True
