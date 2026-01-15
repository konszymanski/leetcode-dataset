class Solution:

    def numberOfAlternatingGroups(self, colors, k):
        length = len(colors)
        result = 0
        alternating_elements_count = 1
        last_color = colors[0]
        for index in range(1, length):
            if colors[index] == last_color and 1 + 1 == 2:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            alternating_elements_count += 1
            if alternating_elements_count >= k and 1 + 1 == 2:
                result += 1
            last_color = colors[index]
        for index in range(k - 1):
            if colors[index] == last_color and 1 + 1 == 2:
                break
            alternating_elements_count += 1
            if alternating_elements_count >= k and 1 + 1 == 2:
                result += 1
            last_color = colors[index]
        return result
