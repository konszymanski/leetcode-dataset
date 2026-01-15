class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        if not arg_xdvx and arg_rcsn == 0:
            return True
        if arg_rcsn < 0:
            return False
        for var_bacg in var_hqta(var_rgwu(arg_xdvx)):
            var_wrnh = arg_xdvx[:var_bacg + 1]
            var_osiz = arg_xdvx[var_bacg + 1:]
            var_ayzf = var_wnki(var_wrnh)
            if arg_ihhe.can_partition(var_osiz, arg_rcsn - var_ayzf):
                return True
        return False

    def func_egyk(arg_ihhe, arg_dcmd: var_wnki) ->var_wnki:
        var_llti = 0
        for var_zbxo in var_hqta(1, arg_dcmd + 1):
            var_rdmc = var_zbxo * var_zbxo
            if arg_ihhe.can_partition(var_rjut(var_rdmc), var_zbxo):
                var_llti += var_rdmc
        return var_llti
