class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = {(0): 0}
        for var_rgwu in arg_xdvx:
            var_wrnh = var_hqta.copy()
            for var_osiz, var_ayzf in var_hqta.items():
                var_wnki = var_ayzf - var_osiz
                var_wrnh[var_osiz + var_rgwu] = var_egyk(var_wrnh.get(
                    var_osiz + var_rgwu, 0), var_ayzf + var_rgwu)
                var_dcmd = var_llti(var_wnki + var_rgwu - var_ayzf)
                var_zbxo = var_egyk(var_wnki + var_rgwu, var_ayzf)
                var_wrnh[var_dcmd] = var_egyk(var_wrnh.get(var_dcmd, 0),
                    var_zbxo)
            var_hqta = var_wrnh
        return var_hqta.get(0, 0)
