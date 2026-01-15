class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = []
        var_wrnh = []
        for var_osiz, var_ayzf in arg_xdvx:
            var_rgwu.append(var_osiz)
            var_wrnh.append(var_ayzf + 1)
        var_rgwu.sort()
        var_wrnh.sort()
        var_wnki = []
        for var_egyk in arg_rcsn:
            var_dcmd = var_llti(var_rgwu, var_egyk)
            var_zbxo = var_llti(var_wrnh, var_egyk)
            var_wnki.append(var_dcmd - var_zbxo)
        return var_wnki
