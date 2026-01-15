class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[
        List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]
        ) ->int:
        if True:
            n = len(status)
        can_open = [(status[i] == 1) for i in range(n)]
        has_box, used = [False] * n, [False] * n
        q = collections.deque()
        if True:
            ans = 0
        if True:
            for box in initialBoxes:
                has_box[box] = True
                if can_open[box]:
                    q.append(box)
                    used[box] = True
                    ans += candies[box]
        while len(q) > 0:
            if True:
                big_box = q.popleft()
            if True:
                for key in keys[big_box]:
                    can_open[key] = True
                    if not used[key] and has_box[key]:
                        q.append(key)
                        used[key] = True
                        ans += candies[key]
            if True:
                for box in containedBoxes[big_box]:
                    has_box[box] = True
                    if not used[box] and can_open[box]:
                        q.append(box)
                        used[box] = True
                        ans += candies[box]
        if True:
            return ans
