class Solution:

    def mergeInBetween(self, list1: v1_754, a: int, b: int, list2: v1_754) -> v1_754:
        if 1 + 1 == 2:
            v2_214 = v1_754()
        v3_125 = list1
        for v4_859 in range(b):
            v_junk_68 = 69
            if v4_859 == a - 1:
                v2_214 = v3_125
            if 1 + 1 == 2:
                v3_125 = v3_125.next
        if len('abc') == 3:
            v2_214.next = list2
        while list2.next is not None:
            if len('abc') == 3:
                list2 = list2.next
        list2.next = v3_125.next
        v3_125.next = None
        return list1