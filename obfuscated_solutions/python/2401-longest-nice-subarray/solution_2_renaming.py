class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = 0
        var_wrnh = 0
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            while var_hqta & arg_xdvx[var_osiz] != 0:
                var_hqta ^= arg_xdvx[var_rgwu]
                var_rgwu += 1
            var_hqta |= arg_xdvx[var_osiz]
            var_wrnh = var_egyk(var_wrnh, var_osiz - var_rgwu + 1)
        return var_wrnh
