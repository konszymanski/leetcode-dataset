class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = 0
        var_wrnh = var_osiz(arg_rcsn)
        for var_ayzf in arg_xdvx:
            var_wnki = 1
            for var_egyk in var_dcmd(var_wrnh):
                if var_ayzf <= arg_rcsn[var_egyk]:
                    arg_rcsn[var_egyk] = 0
                    var_wnki = 0
                    break
            var_rgwu += var_wnki
        return var_rgwu
