class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = 0
        var_hqta = 0
        while var_bacg < var_rgwu(arg_xdvx) and var_hqta < var_rgwu(arg_rcsn):
            if arg_xdvx[var_bacg] < arg_rcsn[var_hqta]:
                var_bacg += 1
            elif arg_xdvx[var_bacg] > arg_rcsn[var_hqta]:
                var_hqta += 1
            else:
                return arg_xdvx[var_bacg]
        return -1
