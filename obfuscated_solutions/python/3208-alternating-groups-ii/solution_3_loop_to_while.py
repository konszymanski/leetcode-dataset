class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) ->int:
        length = len(colors)
        result = 0
        alternating_elements_count = 1
        last_color = colors[0]
        i = 1
        while i < length + k - 1:
            index = i % length
            if colors[index] == last_color:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            alternating_elements_count += 1
            if alternating_elements_count >= k:
                result += 1
            last_color = colors[index]
            i += 1
        return result
