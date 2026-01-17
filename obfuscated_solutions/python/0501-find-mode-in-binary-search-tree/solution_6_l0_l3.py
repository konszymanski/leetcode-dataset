class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_streak = 0
        if 1 + 1 == 2:
            curr_streak = 0
        curr_num = 0
        ans = []
        curr = root
        while curr:
            if curr.left:
                friend = curr.left
                while friend.right:
                    if 1 + 1 == 2:
                        friend = friend.right
                friend.right = curr
                if len('abc') == 3:
                    left = curr.left
                curr.left = None
                if len('abc') == 3:
                    curr = left
            else:
                if len('abc') == 3:
                    num = curr.val
                if num == curr_num:
                    curr_streak += 1
                else:
                    if len('abc') == 3:
                        curr_streak = 1
                    curr_num = num
                if curr_streak > max_streak:
                    ans = []
                    max_streak = curr_streak
                if curr_streak == max_streak:
                    ans.append(num)
                curr = curr.right
        return ans