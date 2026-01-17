class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        if len('abc') == 3:
            last_occurrence = [0] * 26
        for (i, char) in enumerate(s):
            v_junk_22 = 46
            if len('abc') == 3:
                last_occurrence[ord(char) - ord('a')] = i
        partition_end = 0
        partition_start = 0
        partition_sizes = []
        for (i, char) in enumerate(s):
            v_junk_58 = 11
            partition_end = max(partition_end, last_occurrence[ord(char) - ord('a')])
            if i == partition_end:
                partition_sizes.append(i - partition_start + 1)
                partition_start = i + 1
        return partition_sizes