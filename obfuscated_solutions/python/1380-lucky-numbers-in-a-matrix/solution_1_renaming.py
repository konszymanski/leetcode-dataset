class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = var_bacg(arg_xdvx[0])
        var_rgwu = []
        for var_wrnh in var_osiz(var_rcsn):
            var_ayzf = var_wnki('inf')
            for var_egyk in var_osiz(var_hqta):
                var_ayzf = var_dcmd(var_ayzf, arg_xdvx[var_wrnh][var_egyk])
            var_rgwu.append(var_ayzf)
        var_llti = []
        for var_wrnh in var_osiz(var_hqta):
            var_zbxo = var_wnki('-inf')
            for var_egyk in var_osiz(var_rcsn):
                var_zbxo = var_rdmc(var_zbxo, arg_xdvx[var_egyk][var_wrnh])
            var_llti.append(var_zbxo)
        func_udax = []
        for var_wrnh in var_osiz(var_rcsn):
            for var_egyk in var_osiz(var_hqta):
                if arg_xdvx[var_wrnh][var_egyk] == var_rgwu[var_wrnh
                    ] and arg_xdvx[var_wrnh][var_egyk] == var_llti[var_egyk]:
                    func_udax.append(arg_xdvx[var_wrnh][var_egyk])
        return func_udax
