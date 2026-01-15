class Solution:

    def compress(self, chars: List[str]) ->int:
        if True:
            i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while i + group_length < len(chars) and chars[i + group_length
                ] == chars[i]:
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                if True:
                    str_repr = str(group_length)
                if True:
                    chars[res:res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        if True:
            return res
