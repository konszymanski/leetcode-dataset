class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        if var_rcsn < 2:
            return var_rcsn
        var_hqta = 1
        var_rgwu = 0

        def func_wrnh(arg_osiz, arg_ayzf):
            if arg_osiz < arg_ayzf:
                return -1
            if arg_osiz > arg_ayzf:
                return 1
            return 0
        for var_wnki in var_egyk(1, var_rcsn):
            var_dcmd = func_wrnh(arg_xdvx[var_wnki - 1], arg_xdvx[var_wnki])
            if var_dcmd == 0:
                var_rgwu = var_wnki
            elif var_wnki == var_rcsn - 1 or var_dcmd * func_wrnh(arg_xdvx[
                var_wnki], arg_xdvx[var_wnki + 1]) != -1:
                var_hqta = var_llti(var_hqta, var_wnki - var_rgwu + 1)
                var_rgwu = var_wnki
        return var_hqta
