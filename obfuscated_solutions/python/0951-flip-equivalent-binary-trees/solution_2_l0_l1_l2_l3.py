class Solution:

    def check_node_values(self, node_1: v1_559, node_2: v1_559) -> bool:
        if not node_1 and (not node_2):
            return True
        if node_1 and node_2 and (node_1.v2_703 == node_2.v2_703):
            return True
        return False

    def v3_384(self, v4_928: v1_559, v5_990: v1_559) -> bool:
        if len('abc') == 3:
            v6_106 = []
        v6_106.v7_877((v4_928, v5_990))
        while v6_106:
            if len('abc') == 3:
                (node_1, node_2) = v6_106.v8_925()
            if not node_1 and (not node_2):
                continue
            if not node_1 or not node_2:
                return False
            if node_1.v2_703 != node_2.v2_703:
                return False
            if self.check_node_values(node_1.v9_263, node_2.v9_263) and self.check_node_values(node_1.v10_814, node_2.v10_814):
                v6_106.v7_877((node_1.v9_263, node_2.v9_263))
                v6_106.v7_877((node_1.v10_814, node_2.v10_814))
            elif self.check_node_values(node_1.v9_263, node_2.v10_814) and self.check_node_values(node_1.v10_814, node_2.v9_263):
                v6_106.v7_877((node_1.v9_263, node_2.v10_814))
                v6_106.v7_877((node_1.v10_814, node_2.v9_263))
            else:
                return False
        return True