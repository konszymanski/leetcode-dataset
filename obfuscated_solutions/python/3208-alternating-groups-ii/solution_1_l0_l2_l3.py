class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            v_junk_53 = 36
            colors.append(colors[i])
        if len('abc') == 3:
            length = len(colors)
        if len('abc') == 3:
            result = 0
        if len('abc') == 3:
            left = 0
        right = 1
        while right < length:
            if colors[right] == colors[right - 1]:
                left = right
                right = right + 1
                continue
            right = right + 1
            if right - left < k:
                continue
            result = result + 1
            left = left + 1
        return result