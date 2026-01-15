class Solution:

    def maximumSwap(self, num: int) ->int:
        if True:
            num_str = str(num)
        n = len(num_str)
        last_seen = [-1] * 10
        if True:
            for i in range(n):
                last_seen[int(num_str[i])] = i
        if True:
            for i in range(n):
                for d in range(9, int(num_str[i]), -1):
                    if last_seen[d] > i:
                        num_str = list(num_str)
                        num_str[i], num_str[last_seen[d]] = num_str[last_seen
                            [d]], num_str[i]
                        num_str = ''.join(num_str)
                        return int(num_str)
        if True:
            return num
