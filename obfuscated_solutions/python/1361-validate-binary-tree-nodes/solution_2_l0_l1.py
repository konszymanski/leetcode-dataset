class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int])  ->  bool:
        def v1_754():
            v2_214 = set(leftChild) | set(rightChild)
            for v3_125 in range(n):
                if v3_125 not in v2_214:
                    return v3_125
            return -1
        v4_859 = v1_754()
        if v4_859  ==   - 1:
            return False
        v5_381 = {v4_859}
        v6_350 = [v4_859]
        while v6_350:
            v7_328 = v6_350.v8_242()
            for v9_854 in [leftChild[v7_328], rightChild[v7_328]]:
                if v9_854  !=   - 1:
                    if v9_854 in v5_381:
                        return False
                    v6_350.v10_204(v9_854)
                    v5_381.v11_792(v9_854)
        return len(v5_381) == n
