class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in var_wrnh(2, var_osiz(arg_xdvx)):
            if arg_xdvx[var_rgwu - 2] == 0:
                var_hqta += 1
                arg_xdvx[var_rgwu - 2] = arg_xdvx[var_rgwu - 2] ^ 1
                arg_xdvx[var_rgwu - 1] = arg_xdvx[var_rgwu - 1] ^ 1
                arg_xdvx[var_rgwu] = arg_xdvx[var_rgwu] ^ 1
        if var_ayzf(arg_xdvx) == var_osiz(arg_xdvx):
            return var_hqta
        return -1
