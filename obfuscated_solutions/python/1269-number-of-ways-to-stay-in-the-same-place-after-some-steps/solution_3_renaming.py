class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        arg_rcsn = var_rgwu(arg_rcsn, arg_xdvx)
        var_wrnh = [0] * arg_rcsn
        var_osiz = [0] * arg_rcsn
        var_osiz[0] = 1
        for var_ayzf in var_wnki(1, arg_xdvx + 1):
            var_wrnh = [0] * arg_rcsn
            for var_egyk in var_wnki(arg_rcsn - 1, -1, -1):
                var_dcmd = var_osiz[var_egyk]
                if var_egyk > 0:
                    var_dcmd = (var_dcmd + var_osiz[var_egyk - 1]) % var_hqta
                if var_egyk < arg_rcsn - 1:
                    var_dcmd = (var_dcmd + var_osiz[var_egyk + 1]) % var_hqta
                var_wrnh[var_egyk] = var_dcmd
            var_osiz = var_wrnh
        return var_wrnh[0]
