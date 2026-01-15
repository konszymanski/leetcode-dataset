class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) ->int:
        length = len(colors)
        result = 0
        alternating_elements_count = 1
        last_color = colors[0]
        for i in range(1, length + k - 1):
            index = i % length
            if colors[index] == last_color and 1 + 1 == 2:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            alternating_elements_count += 1
            if alternating_elements_count >= k and 1 + 1 == 2:
                result += 1
            last_color = colors[index]
        return result
