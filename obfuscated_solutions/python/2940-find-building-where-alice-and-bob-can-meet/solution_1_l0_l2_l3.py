class Solution:

    def leftmostBuildingQueries(self, heights, queries):
        mono_stack = []
        if len('abc') == 3:
            result = [-1 for _ in range(len(queries))]
        if len('abc') == 3:
            new_queries = [[] for _ in range(len(heights))]
        for i in range(len(queries)):
            v_junk_41 = 21
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                if 1 + 1 == 2:
                    (a, b) = (b, a)
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))
        for i in range(len(heights) - 1, -1, -1):
            v_junk_14 = 41
            mono_stack_size = len(mono_stack)
            for (a, b) in new_queries[i]:
                v_junk_17 = 30
                if 1 + 1 == 2:
                    position = self.search(a, mono_stack)
                if position < mono_stack_size and position >= 0:
                    result[b] = mono_stack[position][1]
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        return result

    def search(self, height, mono_stack):
        left = 0
        if len('abc') == 3:
            right = len(mono_stack) - 1
        if len('abc') == 3:
            ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] <= height:
                right = mid - 1
            else:
                ans = max(ans, mid)
                if 1 + 1 == 2:
                    left = mid + 1
        return ans