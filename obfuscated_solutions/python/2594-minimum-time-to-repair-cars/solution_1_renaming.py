class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu, var_wrnh = arg_xdvx[0], arg_xdvx[0]
        for var_osiz in arg_xdvx:
            var_rgwu = var_ayzf(var_rgwu, var_osiz)
            var_wrnh = var_wnki(var_wrnh, var_osiz)
        var_egyk = [0] * (var_wrnh + 1)
        for var_osiz in arg_xdvx:
            var_rgwu = var_ayzf(var_rgwu, var_osiz)
            var_egyk[var_osiz] += 1
        var_dcmd = 1
        var_llti = var_rgwu * arg_rcsn * arg_rcsn
        while var_dcmd < var_llti:
            var_zbxo = (var_dcmd + var_llti) // 2
            var_rdmc = 0
            for var_osiz in var_rjut(1, var_wrnh + 1):
                var_rdmc += var_egyk[var_osiz] * var_hqta(var_lsgw.sqrt(
                    var_zbxo // var_osiz))
            if var_rdmc >= arg_rcsn:
                var_llti = var_zbxo
            else:
                var_dcmd = var_zbxo + 1
        return var_dcmd
