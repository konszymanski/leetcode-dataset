class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_rcsn)
        var_ayzf = [0] * var_rgwu
        for var_wnki in var_egyk(var_wrnh):
            var_dcmd = 0
            for var_llti in var_egyk(var_rgwu):
                var_dcmd = var_zbxo(var_dcmd, var_ayzf[var_llti]) + arg_xdvx[
                    var_llti] * arg_rcsn[var_wnki]
            var_ayzf[var_rgwu - 1] = var_dcmd
            for var_llti in var_egyk(var_rgwu - 2, -1, -1):
                var_ayzf[var_llti] = var_ayzf[var_llti + 1] - arg_xdvx[
                    var_llti + 1] * arg_rcsn[var_wnki]
        return var_ayzf[var_rgwu - 1]
