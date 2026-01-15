class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        for var_rcsn in var_bacg(2, var_hqta(arg_xdvx) + 1):
            if arg_xdvx % var_rcsn == 0:
                return False
        return True

    def func_rgwu(arg_ihhe, arg_wrnh):
        var_osiz = var_ayzf(arg_wrnh)
        var_wnki = [0] * (var_osiz + 1)
        for var_rcsn in var_bacg(2, var_osiz + 1):
            if arg_ihhe.isprime(var_rcsn):
                var_wnki[var_rcsn] = var_rcsn
            else:
                var_wnki[var_rcsn] = var_wnki[var_rcsn - 1]
        for var_rcsn in var_bacg(var_egyk(arg_wrnh)):
            if var_rcsn == 0:
                var_dcmd = arg_wrnh[0]
            else:
                var_dcmd = arg_wrnh[var_rcsn] - arg_wrnh[var_rcsn - 1]
            if var_dcmd <= 0:
                return False
            var_llti = var_wnki[var_dcmd - 1]
            arg_wrnh[var_rcsn] -= var_llti
        return True
