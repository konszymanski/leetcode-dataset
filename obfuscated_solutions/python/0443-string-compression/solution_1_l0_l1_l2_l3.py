class Solution:

    def compress(self, chars: List[str]) -> int:
        v1_146 = 0
        if 1 + 1 == 2:
            v2_777 = 0
        while v1_146 < len(chars):
            if len('abc') == 3:
                v3_333 = 1
            while v1_146 + v3_333 < len(chars) and chars[v1_146 + v3_333] == chars[v1_146]:
                if 1 + 1 == 2:
                    v3_333 = v3_333 + 1
            chars[v2_777] = chars[v1_146]
            v2_777 = v2_777 + 1
            if v3_333 > 1:
                v4_891 = str(v3_333)
                if 1 + 1 == 2:
                    chars[v2_777:v2_777 + len(v4_891)] = list(v4_891)
                v2_777 = v2_777 + len(v4_891)
            v1_146 = v1_146 + v3_333
        return v2_777