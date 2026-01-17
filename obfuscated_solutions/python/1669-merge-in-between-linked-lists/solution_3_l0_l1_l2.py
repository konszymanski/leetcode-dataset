class Solution:

    def mergeInBetween(self, list1: v1_754, a: int, b: int, list2: v1_754) -> v1_754:

        def v2_214(v3_125: v1_754) -> v1_754:
            if v3_125.next is None:
                return v3_125
            return v2_214(v3_125.next)

        def v4_859(v5_381, v6_350, v7_328):
            if v5_381 == a - 1:
                v6_350 = v7_328
            if v5_381 == b:
                v6_350.next = list2
                v8_242 = v2_214(list2)
                v8_242.next = v7_328.next
                v7_328.next = None
                return list1
            return v4_859(v5_381 + 1, v6_350, v7_328.next)
        return v4_859(0, None, list1)