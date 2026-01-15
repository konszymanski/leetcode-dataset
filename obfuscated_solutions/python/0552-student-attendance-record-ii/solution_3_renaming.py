class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 1000000007
        var_hqta = [([0] * 3) for var_rgwu in var_wrnh(2)]
        var_osiz = [([0] * 3) for var_rgwu in var_wrnh(2)]
        var_hqta[0][0] = 1
        for var_rgwu in var_wrnh(arg_xdvx):
            for var_ayzf in var_wrnh(2):
                for var_wnki in var_wrnh(3):
                    var_osiz[var_ayzf][0] = (var_osiz[var_ayzf][0] +
                        var_hqta[var_ayzf][var_wnki]) % var_bacg
                    if var_ayzf < 1:
                        var_osiz[var_ayzf + 1][0] = (var_osiz[var_ayzf + 1]
                            [0] + var_hqta[var_ayzf][var_wnki]) % var_bacg
                    if var_wnki < 2:
                        var_osiz[var_ayzf][var_wnki + 1] = (var_osiz[
                            var_ayzf][var_wnki + 1] + var_hqta[var_ayzf][
                            var_wnki]) % var_bacg
            var_hqta = [var_egyk[:] for var_egyk in var_osiz]
            var_osiz = [([0] * 3) for var_rgwu in var_wrnh(2)]
        var_dcmd = var_llti(var_hqta[var_ayzf][var_wnki] for var_ayzf in
            var_wrnh(2) for var_wnki in var_wrnh(3)) % var_bacg
        return var_dcmd
