class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_rjut[
        var_bacg]:
        if arg_xdvx == 1:
            return [var_hqta for var_hqta in var_rgwu(10)]
        var_wrnh = []

        def func_osiz(arg_xdvx, arg_ayzf):
            if arg_xdvx == 0:
                return var_wrnh.append(arg_ayzf)
            var_wnki = arg_ayzf % 10
            var_egyk = var_dcmd([var_wnki + arg_rcsn, var_wnki - arg_rcsn])
            for var_llti in var_egyk:
                if 0 <= var_llti < 10:
                    var_zbxo = arg_ayzf * 10 + var_llti
                    func_osiz(arg_xdvx - 1, var_zbxo)
        for arg_ayzf in var_rgwu(1, 10):
            func_osiz(arg_xdvx - 1, arg_ayzf)
        return var_rdmc(var_wrnh)
