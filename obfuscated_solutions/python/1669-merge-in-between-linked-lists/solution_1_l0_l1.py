class Solution:
    def mergeInBetween(self, list1: v1_754, a: int, b: int, list2: v1_754)  ->  v1_754:
        v2_214 = []
        v3_125 = 0
        v4_859 = list1
        while v3_125 < a:
            v2_214.v5_381(v4_859.v6_350)
            v4_859 = v4_859.next
            v3_125  +=  1
        v7_328 = list2
        while v7_328 is not None:
            v2_214.v5_381(v7_328.v6_350)
            v7_328 = v7_328.next
        while v3_125 < b + 1:
            v4_859 = v4_859.next
            v3_125  +=  1
        while v4_859 is not None:
            v2_214.v5_381(v4_859.v6_350)
            v4_859 = v4_859.next
        v8_242 = None
        for v9_854 in range(len(v2_214)):
            v10_204 = v1_754(v2_214.v11_792(), v8_242)
            v8_242 = v10_204
        return v8_242
