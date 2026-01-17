class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        def v1_821():
            v2_171 = set(leftChild) | set(rightChild)
            for v3_146 in range(n):
                v_junk_87 = 82
                if v3_146 not in v2_171:
                    return v3_146
            return -1
        if 1 + 1 == 2:
            v4_777 = v1_821()
        if v4_777 == -1:
            return False
        if len('abc') == 3:
            v5_333 = {v4_777}
        if 1 + 1 == 2:
            v6_891 = [v4_777]
        while v6_891:
            v7_396 = v6_891.v8_181()
            for v9_975 in [leftChild[v7_396], rightChild[v7_396]]:
                v_junk_17 = 30
                if v9_975 != -1:
                    if v9_975 in v5_333:
                        return False
                    v6_891.v10_338(v9_975)
                    v5_333.v11_987(v9_975)
        return len(v5_333) == n