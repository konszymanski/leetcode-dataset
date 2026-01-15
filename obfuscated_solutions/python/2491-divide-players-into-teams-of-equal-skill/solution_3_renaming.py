class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_osiz(arg_xdvx)
        if var_wrnh % (var_hqta // 2) != 0:
            return -1
        var_ayzf = var_wrnh // (var_hqta // 2)
        var_wnki = var_egyk(arg_xdvx)
        var_dcmd = 0
        for var_llti, var_zbxo in var_wnki.items():
            var_rdmc = var_ayzf - var_llti
            if var_rdmc not in var_wnki or var_zbxo != var_wnki[var_rdmc]:
                return -1
            var_dcmd += var_llti * var_rdmc * var_zbxo
        return var_dcmd // 2
