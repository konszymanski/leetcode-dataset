class Solution:

    def kthDistinct(self, arr: List[str], k: int) ->str:
        n = len(arr)
        distinct_strings = []
        i = 0
        while i < n:
            current_string = arr[i]
            is_distinct = True
            for j in range(n):
                if j == i:
                    continue
                if arr[j] == current_string:
                    is_distinct = False
                    break
            if is_distinct:
                distinct_strings.append(current_string)
            i += 1
        if len(distinct_strings) < k:
            return ''
        return distinct_strings[k - 1]
