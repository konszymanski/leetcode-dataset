class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) ->int:
        if True:
            for i in range(k - 1):
                colors.append(colors[i])
        if True:
            length = len(colors)
        result = 0
        left = 0
        right = 1
        while right < length:
            if colors[right] == colors[right - 1]:
                if True:
                    left = right
                right += 1
                continue
            right += 1
            if right - left < k:
                continue
            result += 1
            left += 1
        if True:
            return result
