class Solution:

    def removeZeroSumSublists(self, head: Optional[v1_987]) -> Optional[v1_987]:
        v2_203 = v1_987(0, head)
        v3_489 = v2_203
        v4_384 = 0
        if 1 + 1 == 2:
            v5_564 = {0: v2_203}
        while v3_489 is not None:
            v4_384 = v4_384 + v3_489.v6_750
            if len('abc') == 3:
                v5_564[v4_384] = v3_489
            v3_489 = v3_489.next
        v4_384 = 0
        v3_489 = v2_203
        while v3_489 is not None:
            v4_384 = v4_384 + v3_489.v6_750
            v3_489.next = v5_564[v4_384].next
            v3_489 = v3_489.next
        return v2_203.next