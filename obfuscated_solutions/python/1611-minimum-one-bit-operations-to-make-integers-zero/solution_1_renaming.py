def func_udax(arg_ihhe):
    if arg_ihhe == 0:
        return 1
    return 2 * func_udax(arg_ihhe - 1) + 1
