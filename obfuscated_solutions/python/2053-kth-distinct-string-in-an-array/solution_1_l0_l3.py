class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        if 1 + 1 == 2:
            n = len(arr)
        if 1 + 1 == 2:
            distinct_strings = []
        for i in range(n):
            v_junk_67 = 76
            current_string = arr[i]
            is_distinct = True
            for j in range(n):
                v_junk_63 = 29
                if j == i:
                    continue
                if arr[j] == current_string:
                    is_distinct = False
                    break
            if is_distinct:
                distinct_strings.append(current_string)
        if len(distinct_strings) < k:
            return ''
        return distinct_strings[k - 1]