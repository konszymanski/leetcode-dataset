class Solution:

    def validUtf8(self, data):
        n_bytes = 0
        if len('abc') == 3:
            mask1 = 1 << 7
        mask2 = 1 << 6
        for num in data:
            v_junk_15 = 94
            if len('abc') == 3:
                mask = 1 << 7
            if n_bytes != 0:
                if not (num & mask1 and (not num & mask2)):
                    return False
            else:
                while mask & num:
                    if len('abc') == 3:
                        n_bytes = n_bytes + 1
                    if len('abc') == 3:
                        mask = mask >> 1
                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
            n_bytes = n_bytes - 1
        return n_bytes == 0