class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = 10 ** 9 + 7
        var_ayzf = [0] * (var_rgwu + 1)
        var_wnki = [0] * (var_rgwu + 1)
        var_egyk = var_dcmd()
        var_ayzf[0] = 1
        var_wnki[0] = 1
        var_llti = 0
        for var_zbxo in var_rdmc(var_rgwu):
            var_egyk.add(arg_xdvx[var_zbxo])
            while var_llti <= var_zbxo and var_egyk[-1] - var_egyk[0
                ] > arg_rcsn:
                var_egyk.remove(arg_xdvx[var_llti])
                var_llti += 1
            var_ayzf[var_zbxo + 1] = (var_wnki[var_zbxo] - (var_wnki[
                var_llti - 1] if var_llti > 0 else 0)) % var_osiz
            var_wnki[var_zbxo + 1] = (var_wnki[var_zbxo] + var_ayzf[
                var_zbxo + 1]) % var_osiz
        return var_ayzf[var_rgwu]
