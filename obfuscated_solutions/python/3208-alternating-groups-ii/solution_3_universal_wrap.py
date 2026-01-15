class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) ->int:
        if True:
            length = len(colors)
        result = 0
        alternating_elements_count = 1
        last_color = colors[0]
        if True:
            for i in range(1, length + k - 1):
                index = i % length
                if colors[index] == last_color:
                    alternating_elements_count = 1
                    last_color = colors[index]
                    continue
                alternating_elements_count += 1
                if alternating_elements_count >= k:
                    result += 1
                last_color = colors[index]
        if True:
            return result
