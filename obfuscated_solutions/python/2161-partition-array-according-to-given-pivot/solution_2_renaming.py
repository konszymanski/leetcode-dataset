class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = 0
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            if var_rgwu < arg_rcsn:
                var_bacg += 1
            elif var_rgwu == arg_rcsn:
                var_hqta += 1
        var_wrnh = [0] * var_osiz(arg_xdvx)
        var_ayzf = 0
        var_wnki = var_bacg
        var_egyk = var_bacg + var_hqta
        for var_dcmd in var_llti(var_osiz(arg_xdvx)):
            var_rgwu = arg_xdvx[var_dcmd]
            if var_rgwu < arg_rcsn:
                var_wrnh[var_ayzf] = var_rgwu
                var_ayzf += 1
            elif var_rgwu > arg_rcsn:
                var_wrnh[var_egyk] = var_rgwu
                var_egyk += 1
            else:
                var_wrnh[var_wnki] = var_rgwu
                var_wnki += 1
        return var_wrnh
