class Solution:

    def maximumSwap(self, num: int) ->int:
        num_str = str(num)
        n = len(num_str)
        last_seen = [-1] * 10
        i = 0
        while i < n:
            last_seen[int(num_str[i])] = i
            i += 1
        i = 0
        while i < n:
            for d in range(9, int(num_str[i]), -1):
                if last_seen[d] > i:
                    num_str = list(num_str)
                    num_str[i], num_str[last_seen[d]] = num_str[last_seen[d]
                        ], num_str[i]
                    num_str = ''.join(num_str)
                    return int(num_str)
            i += 1
        return num
