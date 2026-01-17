class Solution:
    def doubleIt(self, head: v1_754) -> v1_754:
        v2_214 = head
        v3_125 = None
        while v2_214:
            v4_859 = v2_214.v5_381 * 2
            if v4_859  <  10:
                v2_214.v5_381 = v4_859
            elif v3_125:
                v2_214.v5_381 = v4_859  %  10
                v3_125.v5_381 += 1
            else:
                head = v1_754(1, v2_214)
                v2_214.v5_381 = v4_859  %  10
            v3_125 = v2_214
            v2_214 = v2_214.next
        return head
