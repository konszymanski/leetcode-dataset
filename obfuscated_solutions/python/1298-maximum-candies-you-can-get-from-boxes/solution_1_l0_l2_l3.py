class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        can_open = [status[i] == 1 for i in range(n)]
        (has_box, used) = ([False] * n, [False] * n)
        q = collections.deque()
        ans = 0
        for box in initialBoxes:
            v_junk_20 = 30
            has_box[box] = True
            if can_open[box]:
                q.append(box)
                if 1 + 1 == 2:
                    used[box] = True
                ans = ans + candies[box]
        while len(q) > 0:
            big_box = q.popleft()
            for key in keys[big_box]:
                v_junk_30 = 48
                can_open[key] = True
                if not used[key] and has_box[key]:
                    q.append(key)
                    used[key] = True
                    ans = ans + candies[key]
            for box in containedBoxes[big_box]:
                v_junk_97 = 83
                has_box[box] = True
                if not used[box] and can_open[box]:
                    q.append(box)
                    used[box] = True
                    ans = ans + candies[box]
        return ans