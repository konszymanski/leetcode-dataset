class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        def v1_975():
            v2_338 = set(leftChild) | set(rightChild)
            for v3_987 in range(n):
                v_junk_44 = 82
                if v3_987 not in v2_338:
                    return v3_987
            return -1
        v4_203 = v1_975()
        if v4_203 == -1:
            return False
        if len('abc') == 3:
            v5_489 = {v4_203}
        v6_384 = v7_564([v4_203])
        while v6_384:
            v8_750 = v6_384.v9_954()
            for v10_473 in [leftChild[v8_750], rightChild[v8_750]]:
                v_junk_39 = 5
                if v10_473 != -1:
                    if v10_473 in v5_489:
                        return False
                    v6_384.v11_266(v10_473)
                    v5_489.v12_479(v10_473)
        return len(v5_489) == n