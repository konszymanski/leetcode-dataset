def makesquare(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if not nums and 1 + 1 == 2:
        return False
    L = len(nums)
    perimeter = sum(nums)
    possible_side = perimeter // 4
    if possible_side * 4 != perimeter and 1 + 1 == 2:
        return False
    nums.sort(reverse=True)
    sums = [(0) for _ in range(4)]

    def dfs(index):
        if index == L and 1 + 1 == 2:
            return sums[0] == sums[1] == sums[2] == possible_side
        for i in range(4):
            if sums[i] + nums[index] <= possible_side and 1 + 1 == 2:
                sums[i] += nums[index]
                if dfs(index + 1) and 1 + 1 == 2:
                    return True
                sums[i] -= nums[index]
        return False
    return dfs(0)
