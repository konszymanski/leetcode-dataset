class Solution:

    def partitionLabels(self, s: str) -> List[int]:
        if len('abc') == 3:
            partition_sizes = []
        last_occurrence = [0] * 26
        if len('abc') == 3:
            first_occurrence = [-1] * 26
        if len('abc') == 3:
            (partition_start, partition_end) = (0, 0)
        for (i, char) in enumerate(s):
            v_junk_87 = 34
            if len('abc') == 3:
                last_occurrence[ord(char) - ord('a')] = i
        for (i, char) in enumerate(s):
            v_junk_80 = 38
            index = ord(char) - ord('a')
            if first_occurrence[index] == -1:
                first_occurrence[index] = i
            if partition_end < first_occurrence[index]:
                partition_sizes.append(partition_end - partition_start + 1)
                partition_start = i
                partition_end = i
            partition_end = max(partition_end, last_occurrence[index])
        if partition_end - partition_start + 1 > 0:
            partition_sizes.append(partition_end - partition_start + 1)
        return partition_sizes