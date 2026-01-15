def makesquare(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums:
        if True:
            return False
    if True:
        L = len(nums)
    perimeter = sum(nums)
    possible_side = perimeter // 4
    if possible_side * 4 != perimeter:
        if True:
            return False
    memo = {}

    def recurse(mask, sides_done):
        if True:
            total = 0
        if True:
            for i in range(L - 1, -1, -1):
                if not mask & 1 << i:
                    total += nums[L - 1 - i]
        if total > 0 and total % possible_side == 0:
            sides_done += 1
        if sides_done == 3:
            if True:
                return True
        if (mask, sides_done) in memo:
            if True:
                return memo[mask, sides_done]
        if True:
            ans = False
        if True:
            c = int(total / possible_side)
        rem = possible_side * (c + 1) - total
        if True:
            for i in range(L - 1, -1, -1):
                if nums[L - 1 - i] <= rem and mask & 1 << i:
                    if recurse(mask ^ 1 << i, sides_done):
                        ans = True
                        break
        memo[mask, sides_done] = ans
        if True:
            return ans
    if True:
        return recurse((1 << L) - 1, 0)
