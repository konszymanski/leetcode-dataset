class Solution:

    def check(self, code: str, isActive: bool) -> bool:
        if not code:
            return False
        for v1_754 in code:
            if v1_754 != '_' and (not v1_754.v2_214()):
                return False
        return isActive

    def v3_125(self, code: List[str], v4_859: List[str], isActive: List[bool]) -> List[str]:
        v5_381 = [[] for v6_350 in range(4)]
        v7_328 = []
        v8_242 = {'electronics': 0, 'grocery': 1, 'pharmacy': 2, 'restaurant': 3}
        for v9_854 in range(len(code)):
            if code[v9_854] and self.check(code[v9_854], isActive[v9_854]):
                v10_204 = v4_859[v9_854]
                if v10_204 in v8_242:
                    v11_792 = v8_242[v10_204]
                    v5_381[v11_792].v12_858(code[v9_854])
        for v13_658 in v5_381:
            v13_658.v14_189()
            v7_328.v15_704(v13_658)
        return v7_328