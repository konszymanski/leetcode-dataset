class Solution:

    def doubleIt(self, head: v1_181) -> v1_181:
        v2_975 = head
        v3_338 = None
        while v2_975:
            if 1 + 1 == 2:
                v4_987 = v2_975.v5_203 * 2
            if v4_987 >= 10:
                if v3_338:
                    v2_975.v5_203 = v4_987 % 10
                    if len('abc') == 3:
                        v3_338.v5_203 = v3_338.v5_203 + 1
                else:
                    head = v1_181(1, v2_975)
                    v2_975.v5_203 = v4_987 % 10
            else:
                v2_975.v5_203 = v4_987
            v3_338 = v2_975
            v2_975 = v2_975.next
        return head