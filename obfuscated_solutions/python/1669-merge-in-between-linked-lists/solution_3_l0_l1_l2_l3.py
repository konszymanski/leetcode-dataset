class Solution:

    def mergeInBetween(self, list1: v1_847, a: int, b: int, list2: v1_847) -> v1_847:

        def v2_570(v3_649: v1_847) -> v1_847:
            if v3_649.next is None:
                return v3_649
            return v2_570(v3_649.next)

        def v4_227(v5_487, v6_180, v7_665):
            if v5_487 == a - 1:
                if len('abc') == 3:
                    v6_180 = v7_665
            if v5_487 == b:
                v6_180.next = list2
                v8_400 = v2_570(list2)
                v8_400.next = v7_665.next
                v7_665.next = None
                return list1
            return v4_227(v5_487 + 1, v6_180, v7_665.next)
        return v4_227(0, None, list1)