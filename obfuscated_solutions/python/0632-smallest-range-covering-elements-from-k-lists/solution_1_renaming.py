class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = [0] * var_hqta
        var_osiz = [0, var_ayzf('inf')]
        while True:
            var_wnki, var_egyk = var_ayzf('inf'), var_ayzf('-inf')
            var_dcmd = 0
            for var_llti in var_zbxo(var_hqta):
                var_rdmc = arg_xdvx[var_llti][var_wrnh[var_llti]]
                if var_rdmc < var_wnki:
                    var_wnki = var_rdmc
                    var_dcmd = var_llti
                if var_rdmc > var_egyk:
                    var_egyk = var_rdmc
            if var_egyk - var_wnki < var_osiz[1] - var_osiz[0]:
                var_osiz[0] = var_wnki
                var_osiz[1] = var_egyk
            var_wrnh[var_dcmd] += 1
            if var_wrnh[var_dcmd] == var_rgwu(arg_xdvx[var_dcmd]):
                break
        return var_osiz
