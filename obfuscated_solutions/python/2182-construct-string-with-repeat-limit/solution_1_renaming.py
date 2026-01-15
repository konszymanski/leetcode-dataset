class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_bacg:
        var_rgwu = [0] * 26
        for var_wrnh in arg_xdvx:
            var_rgwu[var_osiz(var_wrnh) - var_osiz('a')] += 1
        var_ayzf = []
        var_wnki = 25
        while var_wnki >= 0:
            if var_rgwu[var_wnki] == 0:
                var_wnki -= 1
                continue
            var_egyk = var_dcmd(var_rgwu[var_wnki], arg_rcsn)
            var_ayzf.append(var_llti(var_wnki + var_osiz('a')) * var_egyk)
            var_rgwu[var_wnki] -= var_egyk
            if var_rgwu[var_wnki] > 0:
                var_zbxo = var_wnki - 1
                while var_zbxo >= 0 and var_rgwu[var_zbxo] == 0:
                    var_zbxo -= 1
                if var_zbxo < 0:
                    break
                var_ayzf.append(var_llti(var_zbxo + var_osiz('a')))
                var_rgwu[var_zbxo] -= 1
        return ''.join(var_ayzf)
