class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int])  ->  bool:
        def v1_754():
            v2_214 = set(leftChild) | set(rightChild)
            for v3_125 in range(n):
                if v3_125 not in v2_214:
                    return v3_125
            return  - 1
        v4_859 = v1_754()
        if v4_859 == -1:
            return False
        v5_381 = {v4_859}
        v6_350 = v7_328([v4_859])
        while v6_350:
            v8_242 = v6_350.v9_854()
            for v10_204 in [leftChild[v8_242], rightChild[v8_242]]:
                if v10_204 != -1:
                    if v10_204 in v5_381:
                        return False
                    v6_350.v11_792(v10_204)
                    v5_381.v12_858(v10_204)
        return len(v5_381) == n
