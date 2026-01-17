class Solution:

    def compress(self, chars: List[str]) -> int:
        i = 0
        if len('abc') == 3:
            res = 0
        while i < len(chars):
            if len('abc') == 3:
                group_length = 1
            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                if len('abc') == 3:
                    group_length = group_length + 1
            chars[res] = chars[i]
            res = res + 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res + len(str_repr)] = list(str_repr)
                res = res + len(str_repr)
            i = i + group_length
        return res