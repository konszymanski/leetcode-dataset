class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in arg_xdvx:
            if var_wrnh <= arg_rcsn:
                var_rgwu += 1
            else:
                var_rgwu = 0
            if var_rgwu == arg_bacg:
                var_hqta += 1
                var_rgwu = 0
        return var_hqta

    def func_osiz(arg_ihhe, arg_xdvx, arg_ayzf, arg_bacg):
        if arg_ayzf * arg_bacg > var_wnki(arg_xdvx):
            return -1
        var_egyk = 0
        var_dcmd = var_llti(arg_xdvx)
        func_osiz = -1
        while var_egyk <= var_dcmd:
            arg_rcsn = (var_egyk + var_dcmd) // 2
            if arg_ihhe.get_num_of_bouquets(arg_xdvx, arg_rcsn, arg_bacg
                ) >= arg_ayzf:
                func_osiz = arg_rcsn
                var_dcmd = arg_rcsn - 1
            else:
                var_egyk = arg_rcsn + 1
        return func_osiz
