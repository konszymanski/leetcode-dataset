class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(var_bacg)
        var_wrnh = 10 ** 9 + 7
        var_osiz, var_ayzf = 0, 0
        for var_wnki in arg_xdvx:
            var_hqta[var_wnki[1]] += 1
        for var_egyk in var_hqta.values():
            var_dcmd = var_egyk * (var_egyk - 1) // 2
            var_osiz = (var_osiz + var_dcmd * var_ayzf) % var_wrnh
            var_ayzf = (var_ayzf + var_dcmd) % var_wrnh
        return var_osiz
