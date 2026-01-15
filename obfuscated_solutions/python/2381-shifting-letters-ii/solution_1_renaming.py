class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_rgwu]]) ->var_bacg:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [0] * var_wrnh
        for var_wnki in arg_rcsn:
            if var_wnki[2] == 1:
                var_ayzf[var_wnki[0]] += 1
                if var_wnki[1] + 1 < var_wrnh:
                    var_ayzf[var_wnki[1] + 1] -= 1
            else:
                var_ayzf[var_wnki[0]] -= 1
                if var_wnki[1] + 1 < var_wrnh:
                    var_ayzf[var_wnki[1] + 1] += 1
        var_egyk = var_hqta(arg_xdvx)
        var_dcmd = 0
        for var_llti in var_zbxo(var_wrnh):
            var_dcmd = (var_dcmd + var_ayzf[var_llti]) % 26
            if var_dcmd < 0:
                var_dcmd += 26
            var_rdmc = var_rjut((var_lsgw(arg_xdvx[var_llti]) - var_lsgw(
                'a') + var_dcmd) % 26 + var_lsgw('a'))
            var_egyk[var_llti] = var_rdmc
        return ''.join(var_egyk)
