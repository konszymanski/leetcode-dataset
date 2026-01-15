class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu()
        for var_wrnh in arg_xdvx:
            var_hqta.add(var_osiz(var_wrnh, 2))
        var_ayzf = var_wnki(arg_xdvx)
        for var_wrnh in var_egyk(var_ayzf + 1):
            if var_wrnh not in var_hqta:
                var_dcmd = var_llti(var_wrnh)[2:]
                return '0' * (var_ayzf - var_wnki(var_dcmd)) + var_dcmd
        return ''
