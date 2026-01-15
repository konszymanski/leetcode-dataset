class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rgwu:
        for var_bacg in var_hqta(2, var_rcsn(arg_xdvx ** 0.5) + 1):
            if arg_xdvx % var_bacg == 0:
                return False
        return True

    def func_wrnh(arg_ihhe, arg_osiz: var_ayzf[var_rcsn]) ->var_rgwu:
        for var_bacg in var_hqta(var_wnki(arg_osiz)):
            if var_bacg == 0:
                var_egyk = arg_osiz[0]
            else:
                var_egyk = arg_osiz[var_bacg] - arg_osiz[var_bacg - 1]
            if var_egyk <= 0:
                return False
            var_dcmd = 0
            for var_llti in var_hqta(var_egyk - 1, 1, -1):
                if arg_ihhe.check_prime(var_llti):
                    var_dcmd = var_llti
                    break
            arg_osiz[var_bacg] = arg_osiz[var_bacg] - var_dcmd
        return True
