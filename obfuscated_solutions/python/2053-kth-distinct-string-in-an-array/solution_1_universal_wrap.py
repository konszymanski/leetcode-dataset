class Solution:

    def kthDistinct(self, arr: List[str], k: int) ->str:
        if True:
            n = len(arr)
        distinct_strings = []
        if True:
            for i in range(n):
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
        if len(distinct_strings) < k:
            if True:
                return ''
        if True:
            return distinct_strings[k - 1]
