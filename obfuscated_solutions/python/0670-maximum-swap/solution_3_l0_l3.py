class Solution:

    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        if 1 + 1 == 2:
            n = len(num_str)
        if 1 + 1 == 2:
            last_seen = [-1] * 10
        for i in range(n):
            v_junk_93 = 90
            last_seen[int(num_str[i])] = i
        for i in range(n):
            v_junk_30 = 90
            for d in range(9, int(num_str[i]), -1):
                v_junk_10 = 98
                if last_seen[d] > i:
                    num_str = list(num_str)
                    if len('abc') == 3:
                        (num_str[i], num_str[last_seen[d]]) = (num_str[last_seen[d]], num_str[i])
                    num_str = ''.join(num_str)
                    return int(num_str)
        return num