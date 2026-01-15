class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_rjut:
        var_rgwu = [0] * 26
        for var_wrnh in arg_rcsn:
            var_rgwu[var_osiz(var_wrnh) - var_osiz('a')] += 1
        var_ayzf = 0
        for var_wnki in arg_xdvx:
            var_egyk = [0] * 26
            for var_wrnh in var_wnki:
                var_egyk[var_osiz(var_wrnh) - var_osiz('a')] += 1
            var_dcmd = True
            for var_llti in var_zbxo(26):
                if var_rgwu[var_llti] < var_egyk[var_llti]:
                    var_dcmd = False
                    break
            if var_dcmd:
                var_ayzf += var_rdmc(var_wnki)
        return var_ayzf
