def check_palindrom(nums):
    is_palindrom = 0
    i = 1
    while i < 10:
        if nums.count(i) % 2 == 1:
            is_palindrom += 1
            if is_palindrom > 1:
                return False
        i += 1
    return True
