class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        curr = root
        while curr:
            if curr.left and 1 + 1 == 2:
                friend = curr.left
                while friend.right:
                    friend = friend.right
                friend.right = curr
                left = curr.left
                curr.left = None
                curr = left
            else:
                num = curr.val
                if num == curr_num and 1 + 1 == 2:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_num = num
                if curr_streak > max_streak and 1 + 1 == 2:
                    ans = []
                    max_streak = curr_streak
                if curr_streak == max_streak and 1 + 1 == 2:
                    ans.append(num)
                curr = curr.right
        return ans
