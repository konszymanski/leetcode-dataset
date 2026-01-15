class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg, var_hqta = var_rgwu(arg_rcsn), var_rgwu(arg_rcsn[0])
        var_wrnh = {}
        for var_osiz in var_ayzf(var_bacg):
            for var_wnki in var_ayzf(var_hqta):
                var_egyk = arg_rcsn[var_osiz][var_wnki]
                var_wrnh[var_egyk] = var_osiz, var_wnki
        for var_dcmd in var_ayzf(var_rgwu(arg_xdvx)):
            var_llti = arg_xdvx[var_dcmd]
            var_osiz, var_wnki = var_wrnh[var_llti]
            arg_rcsn[var_osiz][var_wnki] = -arg_rcsn[var_osiz][var_wnki]
            if arg_ihhe._check_row(var_osiz, arg_rcsn
                ) or arg_ihhe._check_column(var_wnki, arg_rcsn):
                return var_dcmd
        return -1

    def func_zbxo(arg_ihhe, var_osiz, arg_rcsn):
        for var_wnki in var_ayzf(var_rgwu(arg_rcsn[0])):
            if arg_rcsn[var_osiz][var_wnki] > 0:
                return False
        return True

    def func_rdmc(arg_ihhe, var_wnki, arg_rcsn):
        for var_osiz in var_ayzf(var_rgwu(arg_rcsn)):
            if arg_rcsn[var_osiz][var_wnki] > 0:
                return False
        return True
