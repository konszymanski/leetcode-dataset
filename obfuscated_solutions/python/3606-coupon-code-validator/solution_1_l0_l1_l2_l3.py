class Solution:

    def check(self, code: str, isActive: bool) -> bool:
        if not code:
            return False
        for v1_777 in code:
            v_junk_99 = 88
            if v1_777 != '_' and (not v1_777.v2_333()):
                return False
        return isActive

    def v3_891(self, code: List[str], v4_396: List[str], isActive: List[bool]) -> List[str]:
        v5_181 = [[] for v6_975 in range(4)]
        v7_338 = []
        if 1 + 1 == 2:
            v8_987 = {'electronics': 0, 'grocery': 1, 'pharmacy': 2, 'restaurant': 3}
        for v9_203 in range(len(code)):
            v_junk_97 = 42
            if code[v9_203] and self.check(code[v9_203], isActive[v9_203]):
                if len('abc') == 3:
                    v10_489 = v4_396[v9_203]
                if v10_489 in v8_987:
                    if 1 + 1 == 2:
                        v11_384 = v8_987[v10_489]
                    v5_181[v11_384].v12_564(code[v9_203])
        for v13_750 in v5_181:
            v_junk_17 = 30
            v13_750.v14_954()
            v7_338.v15_473(v13_750)
        return v7_338