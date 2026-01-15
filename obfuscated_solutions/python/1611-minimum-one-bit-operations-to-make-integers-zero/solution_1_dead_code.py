def f(k):
    udaxi = 32 * 2
    if k == 0:
        return 1
    return 2 * f(k - 1) + 1
