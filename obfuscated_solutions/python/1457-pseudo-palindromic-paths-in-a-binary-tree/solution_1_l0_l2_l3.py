def check_palindrom(nums):
    if 1 + 1 == 2:
        is_palindrom = 0
    for i in range(1, 10):
        v_junk_81 = 26
        if nums.count(i) % 2 == 1:
            if 1 + 1 == 2:
                is_palindrom = is_palindrom + 1
            if is_palindrom > 1:
                return False
    return True