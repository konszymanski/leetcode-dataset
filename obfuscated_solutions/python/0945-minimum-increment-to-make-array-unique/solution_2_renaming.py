class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = 0
        var_wnki = [0] * (var_hqta + var_wrnh)
        for var_egyk in arg_xdvx:
            var_wnki[var_egyk] += 1
        for var_dcmd in var_llti(var_rgwu(var_wnki)):
            if var_wnki[var_dcmd] <= 1:
                continue
            var_zbxo = var_wnki[var_dcmd] - 1
            var_wnki[var_dcmd + 1] += var_zbxo
            var_wnki[var_dcmd] = 1
            var_ayzf += var_zbxo
        return var_ayzf
