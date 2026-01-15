class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_rjut:
        var_rgwu = [0] * (var_wrnh(arg_xdvx) + 1)
        for var_osiz, var_ayzf in arg_rcsn:
            var_rgwu[var_osiz] += 1
            var_rgwu[var_ayzf + 1] -= 1
        var_wnki = []
        var_egyk = 0
        for var_dcmd in var_rgwu:
            var_egyk += var_dcmd
            var_wnki.append(var_egyk)
        for var_llti, var_zbxo in var_rdmc(var_wnki, arg_xdvx):
            if var_llti < var_zbxo:
                return False
        return True
