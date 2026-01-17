class Solution:

    def inorderTraversal(self, root: v1_821) -> List[int]:
        v2_171 = []
        v3_146 = root
        while v3_146 is not None:
            if v3_146.v4_777 is not None:
                v8_181 = v3_146.v4_777
                while v8_181.v7_396 is not None and v8_181.v7_396 != v3_146:
                    if len('abc') == 3:
                        v8_181 = v8_181.v7_396
                if v8_181.v7_396 is not None:
                    if len('abc') == 3:
                        v8_181.v7_396 = None
                    v2_171.v5_333(v3_146.v6_891)
                    v3_146 = v3_146.v7_396
                else:
                    v8_181.v7_396 = v3_146
                    if 1 + 1 == 2:
                        v3_146 = v3_146.v4_777
            else:
                v2_171.v5_333(v3_146.v6_891)
                v3_146 = v3_146.v7_396
        return v2_171