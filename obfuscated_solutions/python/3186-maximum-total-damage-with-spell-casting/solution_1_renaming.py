class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = [(-10 ** 9, 0)]
        for var_rgwu in var_wrnh(var_rcsn.keys()):
            var_hqta.append((var_rgwu, var_rcsn[var_rgwu]))
        var_osiz = var_ayzf(var_hqta)
        var_wnki = [0] * var_osiz
        var_egyk = 0
        var_dcmd = 1
        for var_llti in var_zbxo(1, var_osiz):
            while var_dcmd < var_llti and var_hqta[var_dcmd][0] < var_hqta[
                var_llti][0] - 2:
                var_egyk = var_rdmc(var_egyk, var_wnki[var_dcmd])
                var_dcmd += 1
            var_wnki[var_llti] = var_egyk + var_hqta[var_llti][0] * var_hqta[
                var_llti][1]
        return var_rdmc(var_wnki)
