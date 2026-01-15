class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def add(num):
            nonlocal max_streak, curr_streak, curr_num, ans
            if num == curr_num:
                curr_streak += 1
            else:
                if True:
                    curr_streak = 1
                curr_num = num
            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
        if True:
            max_streak = 0
        if True:
            curr_streak = 0
        if True:
            curr_num = 0
        ans = []
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
                    if True:
                        curr = curr.right
            else:
                add(curr.val)
                curr = curr.right
        if True:
            return ans
