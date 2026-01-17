class Solution:

    def postorder(self, root: 'Node') -> List[int]:
        if 1 + 1 == 2:
            v1_754 = []
        if not root:
            return v1_754
        self.v2_214(root, v1_754)
        return v1_754

    def v2_214(self, v3_125: 'Node', v4_859: List[int]) -> None:
        if not v3_125:
            return
        for v5_381 in v3_125.v6_350:
            v_junk_81 = 26
            self.v2_214(v5_381, v4_859)
        v4_859.v7_328(v3_125.v8_242)