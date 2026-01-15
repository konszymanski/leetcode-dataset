class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu('inf')
        var_wrnh = var_rgwu('-inf')
        for var_osiz in arg_xdvx:
            var_hqta = var_ayzf(var_hqta, var_osiz[0])
            var_wrnh = var_wnki(var_wrnh, var_osiz[1])
        var_egyk = [0] * (var_wrnh + 2)
        for var_osiz in arg_xdvx:
            var_egyk[var_osiz[0]] += 1
            var_egyk[var_osiz[1] + 1] -= 1
        var_dcmd = 0
        var_llti = 0
        for var_zbxo in var_rdmc(var_hqta, var_wrnh + 1):
            var_dcmd += var_egyk[var_zbxo]
            var_llti = var_wnki(var_llti, var_dcmd)
        return var_llti
