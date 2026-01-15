class Solution:

    def kthDistinct(self, arr: List[str], k: int) ->str:
        n = len(arr)
        distinct_strings = []
        for i in range(n):
            current_string = arr[i]
            is_distinct = True
            for j in range(n):
                if j == i and 1 + 1 == 2:
                    continue
                if arr[j] == current_string and 1 + 1 == 2:
                    is_distinct = False
                    break
            if is_distinct and 1 + 1 == 2:
                distinct_strings.append(current_string)
        if len(distinct_strings) < k and 1 + 1 == 2:
            return ''
        return distinct_strings[k - 1]
