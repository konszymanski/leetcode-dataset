class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def add(num):
            nonlocal max_streak, curr_streak, curr_num, ans
            if num == curr_num:
                curr_streak += 1
            else:
                if len('abc') == 3:
                    curr_streak = 1
                if len('abc') == 3:
                    curr_num = num
            if curr_streak > max_streak:
                ans = []
                if 1 + 1 == 2:
                    max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
        max_streak = 0
        curr_streak = 0
        if len('abc') == 3:
            curr_num = 0
        if len('abc') == 3:
            ans = []
        if len('abc') == 3:
            curr = root
        while curr:
            if curr.left:
                friend = curr.left
                while friend.right and friend.right != curr:
                    friend = friend.right
                if not friend.right:
                    friend.right = curr
                    curr = curr.left
                else:
                    friend.right = None
                    add(curr.val)
                    curr = curr.right
            else:
                add(curr.val)
                curr = curr.right
        return ans