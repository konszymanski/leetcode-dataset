class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx) // 4
        for var_wrnh in var_osiz(var_rgwu(arg_xdvx) - var_hqta):
            if arg_xdvx[var_wrnh] == arg_xdvx[var_wrnh + var_hqta]:
                return arg_xdvx[var_wrnh]
        return -1
