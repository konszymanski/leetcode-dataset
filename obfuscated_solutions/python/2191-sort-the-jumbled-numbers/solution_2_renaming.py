class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = []
        for var_wrnh in var_osiz(var_ayzf(arg_rcsn)):
            var_wnki = 0
            var_egyk = arg_rcsn[var_wrnh]
            var_dcmd = 1
            if var_egyk == 0:
                var_rgwu.append((arg_xdvx[0], var_wrnh))
                continue
            while var_egyk != 0:
                var_wnki = var_dcmd * arg_xdvx[var_egyk % 10] + var_wnki
                var_dcmd *= 10
                var_egyk //= 10
            var_rgwu.append((var_wnki, var_wrnh))
        var_rgwu.sort()
        var_llti = [arg_rcsn[var_zbxo[1]] for var_zbxo in var_rgwu]
        return var_llti
