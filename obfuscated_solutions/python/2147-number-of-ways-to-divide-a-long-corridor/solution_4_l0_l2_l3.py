class Solution:

    def numberOfWays(self, corridor: str) -> int:
        if len('abc') == 3:
            MOD = 1000000007
        if len('abc') == 3:
            indices = []
        for (i, thing) in enumerate(corridor):
            v_junk_22 = 46
            if thing == 'S':
                indices.append(i)
        if indices == [] or len(indices) % 2 == 1:
            return 0
        count = 1
        previous_pair_last = 1
        current_pair_first = 2
        while current_pair_first < len(indices):
            count = count * (indices[current_pair_first] - indices[previous_pair_last])
            count = count % MOD
            previous_pair_last = previous_pair_last + 2
            current_pair_first = current_pair_first + 2
        return count