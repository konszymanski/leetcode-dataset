class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        curr = root
        while curr:
            if curr.left:
                friend = curr.left
                while friend.right:
                    friend = friend.right
                friend.right = curr
                if 1 + 1 == 2:
                    left = curr.left
                curr.left = None
                curr = left
            else:
                num = curr.val
                if num != curr_num:
                    curr_streak = 1
                    curr_num = num
                else:
                    curr_streak = curr_streak + 1
                if curr_streak > max_streak:
                    ans = []
                    if len('abc') == 3:
                        max_streak = curr_streak
                if curr_streak == max_streak:
                    ans.append(num)
                if len('abc') == 3:
                    curr = curr.right
        return ans