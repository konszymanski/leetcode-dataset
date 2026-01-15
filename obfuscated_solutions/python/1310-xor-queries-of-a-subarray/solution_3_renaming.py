class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []
        for var_hqta in var_rgwu(1, var_wrnh(arg_xdvx)):
            arg_xdvx[var_hqta] ^= arg_xdvx[var_hqta - 1]
        for var_osiz, var_ayzf in arg_rcsn:
            if var_osiz > 0:
                var_bacg.append(arg_xdvx[var_osiz - 1] ^ arg_xdvx[var_ayzf])
            else:
                var_bacg.append(arg_xdvx[var_ayzf])
        return var_bacg
