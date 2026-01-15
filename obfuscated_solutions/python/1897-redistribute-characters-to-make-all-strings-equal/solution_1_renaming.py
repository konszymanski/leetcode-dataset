class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_llti:
        var_hqta = var_rgwu(var_wrnh)
        for var_osiz in arg_xdvx:
            for var_ayzf in var_osiz:
                var_hqta[var_ayzf] += 1
        var_wnki = var_egyk(arg_xdvx)
        for var_dcmd in var_hqta.values():
            if var_dcmd % var_wnki != 0:
                return False
        return True
