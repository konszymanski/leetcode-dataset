class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [arg_xdvx[var_hqta // 4], arg_xdvx[var_hqta // 2],
            arg_xdvx[3 * var_hqta // 4]]
        var_osiz = var_hqta / 4
        for var_ayzf in var_wrnh:
            var_wnki = var_egyk(arg_xdvx, var_ayzf)
            var_dcmd = var_llti(arg_xdvx, var_ayzf) - 1
            if var_dcmd - var_wnki + 1 > var_osiz:
                return var_ayzf
        return -1
