class Solution:

    def numberOfAlternatingGroups(self, colors, k):
        length = len(colors)
        result = 0
        alternating_elements_count = 1
        last_color = colors[0]
        index = 1
        while index < length:
            if colors[index] == last_color:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            alternating_elements_count += 1
            if alternating_elements_count >= k:
                result += 1
            last_color = colors[index]
            index += 1
        index = 0
        while index < k - 1:
            if colors[index] == last_color:
                break
            alternating_elements_count += 1
            if alternating_elements_count >= k:
                result += 1
            last_color = colors[index]
            index += 1
        return result
