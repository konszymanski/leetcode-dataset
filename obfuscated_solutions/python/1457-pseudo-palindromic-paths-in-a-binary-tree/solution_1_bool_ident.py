def check_palindrom(nums):
    is_palindrom = 0
    for i in range(1, 10):
        if nums.count(i) % 2 == 1 and 1 + 1 == 2:
            is_palindrom += 1
            if is_palindrom > 1 and 1 + 1 == 2:
                return False
    return True
