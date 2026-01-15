def func_udax(arg_ihhe):
    if arg_ihhe < 0:
        return 0
    return arg_ihhe * (arg_ihhe - 1) // 2


class Solution:

    def func_xdvx(arg_rcsn, arg_bacg: var_rgwu, arg_hqta: var_rgwu) ->var_rgwu:
        return func_udax(arg_bacg + 2) - 3 * func_udax(arg_bacg - arg_hqta + 1
            ) + 3 * func_udax(arg_bacg - (arg_hqta + 1) * 2 + 2) - func_udax(
            arg_bacg - 3 * (arg_hqta + 1) + 2)
