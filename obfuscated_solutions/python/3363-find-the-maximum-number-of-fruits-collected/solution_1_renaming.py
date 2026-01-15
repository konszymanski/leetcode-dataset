class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = var_rgwu(arg_xdvx[var_wrnh][var_wrnh] for var_wrnh in
            var_osiz(var_rcsn))

        def func_ayzf():
            var_wnki = [var_egyk('-inf')] * var_rcsn
            var_dcmd = [var_egyk('-inf')] * var_rcsn
            var_wnki[var_rcsn - 1] = arg_xdvx[0][var_rcsn - 1]
            for var_wrnh in var_osiz(1, var_rcsn - 1):
                for var_llti in var_osiz(var_zbxo(var_rcsn - 1 - var_wrnh, 
                    var_wrnh + 1), var_rcsn):
                    var_rdmc = var_wnki[var_llti]
                    if var_llti - 1 >= 0:
                        var_rdmc = var_zbxo(var_rdmc, var_wnki[var_llti - 1])
                    if var_llti + 1 < var_rcsn:
                        var_rdmc = var_zbxo(var_rdmc, var_wnki[var_llti + 1])
                    var_dcmd[var_llti] = var_rdmc + arg_xdvx[var_wrnh][var_llti
                        ]
                var_wnki, var_dcmd = var_dcmd, var_wnki
            return var_wnki[var_rcsn - 1]
        var_hqta += func_ayzf()
        for var_wrnh in var_osiz(var_rcsn):
            for var_llti in var_osiz(var_wrnh):
                arg_xdvx[var_wrnh][var_llti], arg_xdvx[var_llti][var_wrnh
                    ] = arg_xdvx[var_llti][var_wrnh], arg_xdvx[var_wrnh][
                    var_llti]
        var_hqta += func_ayzf()
        return var_hqta
