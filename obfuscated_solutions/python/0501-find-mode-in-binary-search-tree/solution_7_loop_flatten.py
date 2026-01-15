class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def add(num):
            nonlocal max_streak, curr_streak, curr_num, ans
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num
            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        curr = root
        while True:
            if not curr:
                break
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
