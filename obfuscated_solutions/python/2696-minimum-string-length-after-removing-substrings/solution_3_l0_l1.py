class Solution:
    def minLength(self, s: str)  ->  int:
        v1_754 = list(s)
        v2_214 = 0
        for v3_125 in range(len(s)):
            v1_754[v2_214] = v1_754[v3_125]
            if (
                v2_214  >  0
                and v1_754[v2_214  -  1] in "AC"
                and ord(v1_754[v2_214])
                == ord(v1_754[v2_214  -  1]) + 1
            ):
                v2_214 -= 1
            else:
                v2_214 += 1
        return v2_214
