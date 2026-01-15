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
    nums.sort(reverse=True)
    sums = [(0) for _ in range(4)]

    def dfs(index):
        if index == L:
            if True:
                return sums[0] == sums[1] == sums[2] == possible_side
        if True:
            for i in range(4):
                if sums[i] + nums[index] <= possible_side:
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= nums[index]
        if True:
            return False
    if True:
        return dfs(0)
