class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        for var_hqta in var_rgwu(1, arg_xdvx + 1):
            var_bacg = (var_bacg * 10 + 1) % arg_xdvx
            if var_bacg == 0:
                return var_hqta
        return -1
