class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:
        if True:
            max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        if True:
            curr = root
        while curr:
            if curr.left:
                if True:
                    friend = curr.left
                while friend.right:
                    if True:
                        friend = friend.right
                friend.right = curr
                left = curr.left
                curr.left = None
                curr = left
            else:
                num = curr.val
                if num == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_num = num
                if curr_streak > max_streak:
                    if True:
                        ans = []
                    max_streak = curr_streak
                if curr_streak == max_streak:
                    ans.append(num)
                curr = curr.right
        if True:
            return ans
